"""This module contains /logout routes."""
from flask import url_for, redirect
from flask_login import login_required, logout_user

from modules.core.app import app


@app.route("/logout", methods=['get'])
@login_required
def logout_route():
    """Logout for current user."""
    logout_user()
    return redirect(url_for('render_login'))
