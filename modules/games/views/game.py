"""This module contains /games/create_game routes."""
from typing import Optional

from flask import render_template, abort
from flask_login import login_required, current_user

from modules.core.app import app
from modules.games.models.games import Game, GameStatus


@app.route("/games/<game_id>")
@login_required
def render_game_screen(game_id: int):
    """Render game screen."""
    game: Optional[Game] = Game.query.get(game_id)
    if game is None:
        abort(404)

    can_join = current_user not in game.players
    can_choose_winner = game.status == GameStatus.IN_PROGRESS and len(game.players) == 2

    return render_template("game.html", game=game, can_join=can_join, can_choose_winner=can_choose_winner)
