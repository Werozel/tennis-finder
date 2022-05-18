"""This module contains custom error screens."""
from flask import render_template

from modules.core.app_config import AppConfig


@AppConfig.app.errorhandler(400)
def bad_request(_):
    """Render BadRequest error (400)."""
    return render_template("400.html"), 400


@AppConfig.app.errorhandler(403)
def forbidden(_):
    """Render Forbidden error (403)."""
    return render_template("403.html"), 403


@AppConfig.app.errorhandler(404)
def not_found(_):
    """Render NotFound error (404)."""
    return render_template("404.html"), 404


@AppConfig.app.errorhandler(500)
def server_error(_):
    """Render InternalError error (500)."""
    return render_template("500.html"), 500
