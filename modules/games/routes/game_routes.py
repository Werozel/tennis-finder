from typing import Optional

from flask import render_template, abort, redirect, url_for
from flask_login import current_user, login_required

from modules.core.app import app
from modules.core.db import db

from modules.games.models.games import Game, GameStatus
from modules.games.views.find_game import render_find_game


@app.route("/games")
def get_games():
    return []


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
    return redirect(url_for('render_find_game'))


