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

    app: Flask = None
    bootstrap: Bootstrap = None
    login_manager: LoginManager = None
    babel: Babel = None
    db: SQLAlchemy = None

    @staticmethod
    def init():
        cwd = os.getcwd()
        app = Flask(__name__,
                    template_folder=cwd + "/templates",
                    static_folder=cwd + "/static",
                    root_path=cwd)

        app.config['SECRET_KEY'] = SECRET_KEY

        app.jinja_env.globals.update(len=len)
        app.jinja_env.globals.update(is_authenticated=is_authenticated)
        app.jinja_env.globals.update(get_cookie=helpers.args.get_cookie)
        app.jinja_env.globals.update(format_date_time=format_date_time)

        bootstrap = Bootstrap(app)

        login_manager = LoginManager(app)
        login_manager.login_view = 'render_login'
        login_manager.login_message_category = 'warning'
        login_manager.login_message = gettext("Please log in to view this page.")
        login_manager.localize_callback = gettext

        babel = Babel(app)

        @babel.localeselector
        def get_locale():
            """Get babel locale from cookie."""
            return helpers.args.get_cookie('language', 'ru')

        @babel.timezoneselector
        def get_timezone():
            """Get user timezone."""
            user = getattr(g, 'user', None)
            if user is not None:
                return user.timezone

        app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URL
        db = SQLAlchemy(app)
        AppConfig.db = db

        logging.basicConfig(level=logging.DEBUG)
        logging.info("Starting migrations!")
        print("Starting migrations!")
        alembic_args = [
            '--raiseerr',
            'upgrade', 'head',
        ]
        alembic.config.main(argv=alembic_args)

        AppConfig.app = app
        AppConfig.bootstrap = bootstrap
        AppConfig.login_manager = login_manager
        AppConfig.babel = babel
