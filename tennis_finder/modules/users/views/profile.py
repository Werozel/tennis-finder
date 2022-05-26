"""This module contains /profile routes."""
from flask import render_template, abort
from flask_login import login_required, current_user

from tennis_finder.modules.core.app_config import AppConfig
from tennis_finder.modules.users.models.user import User


app = AppConfig.app


@app.route("/profile", methods=['get'])
@login_required
def render_profile():
    """Render current user profile."""
    user = current_user
    games = user.games
    return render_template("profile.html", user=user, my=True, games=games)


@app.route("/profile/<user_id>", methods=['get'])
@login_required
def render_user_profile(user_id: int):
    """Render profile of the user with <user_id>."""
    user = User.query.get(user_id)
    if not user:
        abort(404)
    my = user.id == current_user.id
    return render_template("profile.html", user=user, my=my)
