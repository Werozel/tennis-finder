"""This module contains /profile routes."""
from flask import render_template, abort
from flask_login import login_required, current_user

from modules.core.app import app
from modules.users.models.user import User


@app.route("/profile", methods=['get'])
@login_required
def render_profile():
    """Render /profile view."""
    user = current_user
    games = user.games
    return render_template("profile.html", user=user, my=True, games=games)


@app.route("/profile/<user_id>", methods=['get'])
@login_required
def render_user_profile(user_id: int):
    """Render user with id=user_id profile."""
    user = User.query.get(user_id)
    if not user:
        abort(404)
    my = user.id == current_user.id
    return render_template("profile.html", user=user, my=my)
