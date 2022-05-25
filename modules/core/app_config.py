"""This module contains initial Flask app setup."""
import logging
import os

from flask import Flask, g
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_babel import Babel, gettext
from flask_sqlalchemy import SQLAlchemy

import config
import alembic
import alembic.config
from config import SECRET_KEY
from helpers.datetime_helper import format_date_time
from helpers.user import is_authenticated

import helpers.args


class AppConfig:

    _cwd = os.getcwd()
    app = Flask(__name__,
                template_folder=_cwd + "/templates",
                static_folder=_cwd + "/static",
                root_path=_cwd)
    bootstrap = Bootstrap(app)
    login_manager = LoginManager(app)
    babel = Babel(app)
    db = SQLAlchemy(app)

    @staticmethod
    def init():

        AppConfig.app.config['SECRET_KEY'] = SECRET_KEY

        AppConfig.app.jinja_env.globals.update(len=len)
        AppConfig.app.jinja_env.globals.update(is_authenticated=is_authenticated)
        AppConfig.app.jinja_env.globals.update(get_cookie=helpers.args.get_cookie)
        AppConfig.app.jinja_env.globals.update(format_date_time=format_date_time)

        AppConfig.login_manager.login_view = 'render_login'
        AppConfig.login_manager.login_message_category = 'warning'
        AppConfig.login_manager.login_message = gettext("Please log in to view this page.")
        AppConfig.login_manager.localize_callback = gettext

        AppConfig.app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URL

        logging.basicConfig(level=logging.DEBUG)
        logging.info("Starting migrations!")
        print("Starting migrations!")
        alembic_args = [
            '--raiseerr',
            'upgrade', 'head',
        ]
        alembic.config.main(argv=alembic_args)

    @staticmethod
    @babel.localeselector
    def get_locale():
        """Get babel locale from cookie."""
        return helpers.args.get_cookie('language', 'ru')

    @staticmethod
    @babel.timezoneselector
    def get_timezone():
        """Get user timezone."""
        user = getattr(g, 'user', None)
        if user is not None:
            return user.timezone
