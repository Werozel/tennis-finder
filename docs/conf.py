"""config for sphinx."""

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../tennis_finder'))

# -- Project information -----------------------------------------------------

project = 'Tennis finder'
copyright = '2022, Werozel, cactiw'
author = 'Werozel, cactiw'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

autodoc_mock_imports = [
    "gunicorn",
    "flask",
    "sqlalchemy",
    "Flask-SQLAlchemy",
    "alembic",
    "psycopg2-binary",
    "jinja2",
    "flask-bootstrap",
    "flask-wtf",
    "flask-login",
    "Flask-Babel",
    "googletrans",
    "phonenumbers",
    "WTForms",
    "email_validator",
    "flake8",
    "flake8_docstrings",
    "pytest",
    "faker",
    "pytest-flask-sqlalchemy",
    "numpy",
    "Pillow",
    "flask_wtf",
    "flask_sqlalchemy",
    "flask_bootstrap",
    "flask_babel",
    "flask_login",
    "wtforms",
    "httpcore",
    "werkzeug",
    "Pillow",
    "PIL"
]
