from modules.core.app import app

from modules.games.models.games import Game


@app.route("/games")
def get_games():
    return []

