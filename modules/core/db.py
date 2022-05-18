"""This module contains initial Flask app setup."""
import logging

import alembic
import alembic.config
from flask_sqlalchemy import SQLAlchemy

import config
from modules.core.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URL
db = SQLAlchemy(app)
Base = db.declarative_base()


def init_db():
    """
    Init db and make all pending migrations.

    :return: None
    """
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting migrations!")
    print("Starting migrations!")
    alembic_args = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembic_args)
