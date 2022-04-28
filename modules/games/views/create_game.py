from flask import render_template, make_response, redirect, url_for
from flask_login import login_required, current_user

from helpers.args import get_arg_or_none
from modules.core.app import app
from modules.core.db import db
from modules.games.forms.create_game import CreateGameForm
from modules.games.models.games import Game


@app.route("/games/create_game", methods=['GET'])
@login_required
def render_create_game():
    form = CreateGameForm()
    return render_template("create_game.html", form=form)


@app.route("/games/create_game", methods=['POST'])
@login_required
def create_game():
    form = CreateGameForm()
    user = current_user

    game = Game(name=form.name.data, game_date=form.game_date.data, players=[user])
    db.session.add(game)
    db.session.commit()

    next_page = get_arg_or_none('next')

    return make_response(redirect(next_page) if next_page else redirect(url_for('render_game_screen', game_id=game.id)))
