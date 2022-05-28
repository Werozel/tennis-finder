"""This module contains initial Flask app setup."""
import os

from flask import Flask, g
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_babel import Babel, gettext
from flask_sqlalchemy import SQLAlchemy

import tennis_finder.config as config
from tennis_finder.config import SECRET_KEY
from tennis_finder.helpers.datetime_helper import format_date_time
from tennis_finder.helpers.user import is_authenticated

import tennis_finder.helpers.args


class AppConfig:
    """This is the main config class in the project."""

    _cwd = os.getcwd()
    app = Flask(__name__,
                template_folder=_cwd + "/tennis_finder/templates",
                static_folder=_cwd + "/tennis_finder/static",
                root_path=_cwd)
    bootstrap = Bootstrap(app)
    login_manager = LoginManager(app)
    babel = Babel(app)
    db = None

    @classmethod
    def init(cls):
        """Init app config."""
        cls.app.config['SECRET_KEY'] = SECRET_KEY

        cls.app.jinja_env.globals.update(len=len)
        cls.app.jinja_env.globals.update(is_authenticated=is_authenticated)
        cls.app.jinja_env.globals.update(get_cookie=tennis_finder.helpers.args.get_cookie)
        cls.app.jinja_env.globals.update(format_date_time=format_date_time)

        cls.login_manager.login_view = 'render_login'
        cls.login_manager.login_message_category = 'warning'
        cls.login_manager.login_message = gettext("Please log in to view this page.")
        cls.login_manager.localize_callback = gettext

        cls.app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URL

        cls.db = SQLAlchemy(cls.app)

    @staticmethod
    @babel.localeselector
    def get_locale():
        """Get babel locale from cookie."""
        return tennis_finder.helpers.args.get_cookie('language', 'ru')

    @staticmethod
    @babel.timezoneselector
    def get_timezone():
        """Get user timezone."""
        user = getattr(g, 'user', None)
        if user is not None:
            return user.timezone


AppConfig.init()
