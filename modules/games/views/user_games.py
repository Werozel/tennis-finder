from flask import render_template
from flask_login import current_user, login_required

from modules.core.app import app
from modules.users.models.user import User


@app.route("/my_games", methods=['get'])
@login_required
def render_my_games():
    user: User = current_user
    all_games = user.games
    return render_template("my_games.html", games=all_games)
