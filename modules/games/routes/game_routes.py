"""This module contains /games/* routes."""
from typing import Optional

from flask import abort, redirect, url_for, flash
from flask_babel import gettext
from flask_login import current_user, login_required

from helpers.args import get_arg_or_400
from modules.core.app import app
from modules.core.db import db

from modules.games.models.games import Game, GameStatus
from modules.users.models.user import User


@app.route("/games/join_game/<game_id>")
@login_required
def join_game(game_id: int):
    """Join game with <game_id>."""
    user: User = current_user
    game: Optional[Game] = Game.query.get(game_id)
    if not game:
        abort(404)

    try:
        game.add_player(user)
    except ValueError:
        flash(gettext("You already joined this match"), "info")
        return redirect(url_for("render_game_screen", game_id=game.id))

    db.session.add(game)
    db.session.commit()
    return redirect(url_for('render_game_screen', game_id=game.id))


@app.route("/games/submit_winner/<game_id>")
@login_required
def submit_winner(game_id: int):
    """Set winner in a Game with game_id."""
    user: User = current_user
    game: Game = Game.query.get(game_id)
    if not game:
        abort(404)

    winner_id = get_arg_or_400('winner_id')
    winner = User.query.get(winner_id)
    if not winner:
        abort(404)

    players = game.players
    if user not in players or winner not in players:
        abort(403)

    game.winner_id = winner_id
    game.status = GameStatus.COMPLETED
    db.session.add(game)
    db.session.commit()

    return redirect(url_for('render_game_screen', game_id=game_id))
