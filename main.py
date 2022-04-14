import config
from modules.core.app import app
from modules.core.db import Base, db

# Necessary imports to register
from modules.games.routes import game_routes
from modules.users.routes import user_routes
from modules.users.screens import login, register


def init_db():
    db.create_all()


if __name__ == "__main__":
    init_db()
    app.run(port=config.PORT)
