import pytest
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from modules.core.app_config import AppConfig


@pytest.fixture(scope='session')
def database(request):
    """
    Create a new database for the tests, and drop it when the tests are done.
    """

    @request.addfinalizer
    def drop_database():
        try:
            os.remove("tests/test.sqlite")
        except OSError:
            pass


@pytest.fixture(scope='session')
def app(database):
    """
    Create a Flask app context for the tests.
    """
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.sqlite?check_same_thread=false"

    return app


@pytest.fixture(scope='session')
def _empty_db(app):
    """
    Provide the transactional fixtures with access to the database via a Flask-SQLAlchemy
    database connection.
    """
    db = SQLAlchemy(app=app)

    return db


@pytest.fixture(scope='session')
def _db(_empty_db):
    """
    Provide the transactional fixtures with access to the database via a Flask-SQLAlchemy
    database connection.
    """
    AppConfig.db.metadata.create_all(_empty_db.engine)

    return _empty_db
