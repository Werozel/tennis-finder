import alembic
import alembic.config

import config
from modules.core.app import app
from modules.core.db import db

# Necessary imports to register
from modules.games.routes import game_routes
from modules.users.views import login, register, profile, edit_profile
from modules.users.routes import language, logout
from modules.core.routes import errors
from modules.games.views import game, find_game, create_game


def init_db():
    alembic_args = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembic_args)


if __name__ == "__main__":
    init_db()
    app.run(port=config.PORT, debug=True)
