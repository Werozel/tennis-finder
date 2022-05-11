"""This module contains initial Flask app setup."""
import os

from flask import Flask, g
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_babel import Babel, gettext

from config import SECRET_KEY
from helpers.args import get_cookie
from helpers.datetime_helper import format_date_time
from helpers.user import is_authenticated

cwd = os.getcwd()
app = Flask(__name__,
            template_folder=cwd + "/templates",
            static_folder=cwd + "/static",
            root_path=cwd)
app.config['SECRET_KEY'] = SECRET_KEY

app.jinja_env.globals.update(len=len)
app.jinja_env.globals.update(is_authenticated=is_authenticated)
app.jinja_env.globals.update(get_cookie=get_cookie)
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
    return get_cookie('language', 'ru')


@babel.timezoneselector
def get_timezone():
    """Get user timezone."""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone
