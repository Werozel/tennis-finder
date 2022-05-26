"""This is the main module."""
import alembic.config

import tennis_finder.config as config
from tennis_finder.modules.core.app_config import AppConfig


def init_db():
    alembic_args = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembic_args)


def run_app():
    # Necessary imports to register
    from tennis_finder.modules.games.routes import game_routes
    from tennis_finder.modules.users.views import login, register, profile, edit_profile
    from tennis_finder.modules.users.routes import language, logout
    from tennis_finder.modules.core.routes import errors, index
    from tennis_finder.modules.games.views import game, find_game, create_game, user_games

    __all__ = [
        game_routes, login, register, profile, edit_profile, language, logout, errors,
        game, find_game, create_game, user_games, index
    ]

    AppConfig.app.run(port=config.PORT, debug=False)


if __name__ == "__main__":
    run_app()
