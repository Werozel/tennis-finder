from typing import Optional

from flask import render_template, abort
from flask_login import login_required, current_user

from modules.core.app import app
from modules.games.models.games import Game


@app.route("/games/<game_id>")
@login_required
def render_game_screen(game_id: int):
    game: Optional[Game] = Game.query.get(game_id)
    if game is None:
        abort(404)

    can_join = current_user.id not in map(lambda x: x.id, game.players)

    return render_template("game.html", game=game, can_join=can_join)
