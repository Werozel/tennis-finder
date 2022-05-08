"""This module contains Game models."""
from enum import Enum

from sqlalchemy import func

from modules.core.db import db


class GameStatus(Enum):
    """Game status enum."""

    PENDING = 0  # Waiting for 2nd player
    IN_PROGRESS = 1  # Game in progress
    COMPLETED = 2  # Game completed


game_participants_table = db.Table(
    'game_participants',
    db.Column("game_id", db.INT, db.ForeignKey("games.id")),
    db.Column("user_id", db.INT, db.ForeignKey("users.id")),
)


class Game(db.Model):
    """This is the Game class."""

    __tablename__ = "games"
    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.VARCHAR(512), nullable=False)

    winner_id = db.Column(db.INT, db.ForeignKey("users.id"))
    game_date = db.Column(db.TIMESTAMP)
    status = db.Column(db.Enum(GameStatus), default=GameStatus.PENDING)

    players = db.relationship("User", secondary=game_participants_table, back_populates="games")

    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    updated_at = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def add_player(self, user: 'User'):  # noqa
        """
        Add player to game.

        Throws ValueError if game is not accepting new players or user already joined.
        :param user: User to add
        :return: None
        """
        if self.status != GameStatus.PENDING or user in self.players:
            raise ValueError
        self.players.append(user)
        self.status = GameStatus.IN_PROGRESS
