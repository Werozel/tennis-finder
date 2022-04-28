from typing import Optional

from flask import render_template, abort
from flask_login import login_required

from modules.core.app import app
from modules.games.models.games import Game


@app.route("/games/<game_id>")
@login_required
def render_game_screen(game_id: int):
    game: Optional[Game] = Game.query.get(game_id)
    if game is None:
        abort(404)
    return render_template("game.html", game=game)
