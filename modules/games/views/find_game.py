from flask import render_template
from flask_login import login_required, current_user

from modules.core.app import app
from modules.games.models.games import Game, GameStatus


@app.route("/games/find_game")
@login_required
def render_find_game():
    user = current_user
    games = Game.query.filter(Game.status == GameStatus.PENDING).all()
    return render_template("find_game.html", games=games)
