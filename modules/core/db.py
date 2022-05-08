"""This module contains initial Flask app setup."""
from flask_sqlalchemy import SQLAlchemy

import config
from modules.core.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URL
db = SQLAlchemy(app)
Base = db.declarative_base()
