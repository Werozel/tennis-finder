
from flask import Flask
from flask_bootstrap import Bootstrap

from config import SECRET_KEY

app = Flask(__name__, template_folder="../../templates", static_folder="../../static")
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap(app)
