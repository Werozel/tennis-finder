
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_babel import Babel

from config import SECRET_KEY

app = Flask(__name__, template_folder="../../templates", static_folder="../../static")
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap(app)

login_manager = LoginManager(app)
login_manager.login_view = 'render_login'
login_manager.login_message_category = 'warning'
# TODO: Translate
login_manager.login_message = "Please log in to view this page."
# login_manager.localize_callback = gettext

babel = Babel(app)
