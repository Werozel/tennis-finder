from typing import Optional

from flask import render_template, abort
from flask_login import current_user, login_required

from modules.core.app import app
from modules.core.db import db

from modules.games.models.games import Game, GameStatus


@app.route("/games")
def get_games():
    return []


@app.route("/games/find_game")
@login_required
def render_find_game():
    user = current_user
    games = Game.query.filter(Game.status == GameStatus.PENDING).all()
    return render_template("find_game.html", games=games)


@app.route("/games/join_game/<game_id>")
@login_required
def join_game(game_id: int):
    user = current_user
    game: Optional[Game] = Game.query.get(game_id)
    if game is None:
        abort(404)

    try:
        game.add_player(user)
    except ValueError:
        abort(409)
    db.session.add(game)
    db.session.commit()
    return render_find_game()

