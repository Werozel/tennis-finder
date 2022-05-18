"""This is the main module."""

import config
from modules.core.app import app
from modules.core.db import db, init_db

# Necessary imports to register
from modules.games.routes import game_routes
from modules.users.views import login, register, profile, edit_profile
from modules.users.routes import language, logout
from modules.core.routes import errors
from modules.games.views import game, find_game, create_game, user_games

__all__ = [
    db, game_routes, login, register, profile, edit_profile, language, logout, errors,
    game, find_game, create_game, user_games
]


if __name__ == "__main__":
    init_db()
    app.run(port=config.PORT, debug=False)
