
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_babel import Babel, gettext

from config import SECRET_KEY
from helpers.args import get_cookie
from helpers.user import is_authenticated

app = Flask(__name__, template_folder="../../templates", static_folder="../../static")
app.config['SECRET_KEY'] = SECRET_KEY

app.jinja_env.globals.update(len=len)
app.jinja_env.globals.update(is_authenticated=is_authenticated)
app.jinja_env.globals.update(get_cookie=get_cookie)

bootstrap = Bootstrap(app)

login_manager = LoginManager(app)
login_manager.login_view = 'render_login'
login_manager.login_message_category = 'warning'
login_manager.login_message = gettext("Please log in to view this page.")
login_manager.localize_callback = gettext

babel = Babel(app)


@babel.localeselector
def get_locale():
    return get_cookie('language', 'ru')


@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone
