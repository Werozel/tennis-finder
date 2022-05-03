from typing import Optional

from flask import render_template, abort, redirect, url_for, flash
from flask_babel import gettext
from flask_login import current_user, login_required

from modules.core.app import app
from modules.core.db import db

from modules.games.models.games import Game


@app.route("/games/join_game/<game_id>")
@login_required
def join_game(game_id: int):
    user = current_user
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


@app.route("/games/leave_game/<game_id>")
@login_required
def leave_game(game_id: int):
    user = current_user
    game: Optional[Game] = Game.query.get(game_id)
    if not game:
        abort(404)

    # TODO: @Werozel complete
    return redirect(url_for("render_game_screen", game_id=game.id))
