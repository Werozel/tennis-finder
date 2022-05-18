"""This module contains /games/find_game routes."""
from typing import List

from flask import render_template
from flask_login import login_required, current_user

from modules.core.app_config import AppConfig
from modules.games.models.games import Game, GameStatus
from modules.games.models.search_game import SearchGame
from modules.users.models.user import User


app = AppConfig.app


@app.route("/games/find_game")
@login_required
def render_find_game():
    """Render find game screen."""
    user: User = current_user
    games: List[Game] = Game.query.filter(Game.status == GameStatus.PENDING).all()

    zipped_search_games = []
    for game in games:
        search_game = SearchGame.from_game(game)
        sorting_score = search_game.get_sorting_score(user.skill, user.get_win_rate())
        zipped_search_games.append((search_game, sorting_score))

    sorted_games = list(
        filter(
            lambda x: user not in x.players,
            map(
                lambda x: x[0].game,
                sorted(
                    zipped_search_games,
                    key=lambda x: x[1]
                )
            )
        )
    )

    return render_template("find_game.html", games=sorted_games)
