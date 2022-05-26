"""This module contains /games/create_game routes."""
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from tennis_finder.modules.core.app_config import AppConfig
from tennis_finder.modules.games.forms.create_game import CreateGameForm
from tennis_finder.modules.games.models.games import Game


app = AppConfig.app
db = AppConfig.db


@app.route("/games/create_game", methods=['GET'])
@login_required
def render_create_game():
    """Render create game screen."""
    form = CreateGameForm()
    return render_template("create_game.html", form=form)


@app.route("/games/create_game", methods=['POST'])
@login_required
def create_game():
    """Create new game with provided params."""
    form = CreateGameForm()
    user = current_user

    if not form.validate_on_submit():
        return render_template("create_game.html", form=form)
    game = Game(
        name=form.name.data,
        game_date=form.game_date.data,
        players=[user]
    )
    db.session.add(game)
    db.session.commit()

    return redirect(url_for('render_game_screen', game_id=game.id))
