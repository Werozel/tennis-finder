from flask_login import UserMixin
from sqlalchemy import func

from modules.core.app import login_manager
from modules.core.db import db
from modules.games.models.games import game_participants_table


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.INT, primary_key=True)
    full_name = db.Column(db.VARCHAR(100), nullable=False)
    login = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(512), nullable=False)
    email = db.Column(db.VARCHAR(100))
    phone = db.Column(db.VARCHAR(12))
    skill = db.Column(db.FLOAT, nullable=False)

    wins = db.Column(db.INT, default=0)
    losses = db.Column(db.INT, default=0)

    games = db.relationship("Game", secondary=game_participants_table, back_populates="players")

    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    updated_at = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def __eq__(self, other):
        return self.id == other.id
