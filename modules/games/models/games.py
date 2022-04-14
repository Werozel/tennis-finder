from enum import Enum

import sqlalchemy
from sqlalchemy import Column, INT, ForeignKey, TIMESTAMP, BOOLEAN, Table, func
from sqlalchemy.orm import relationship

from modules.core.db import Base


class GameStatus(Enum):
    PENDING = 0  # Waiting for 2nd player
    IN_PROGRESS = 1  # Game in progress
    COMPLETED = 2  # Game completed
    CANCELED = 3  # Game canceled


game_participants_table = Table(
    'game_participants', Base.metadata,
    Column("game_id", INT, ForeignKey("games.id")),
    Column("user_id", INT, ForeignKey("users.id")),
)


class Game(Base):
    __tablename__ = "games"
    id = Column(INT, primary_key=True)

    winner_id = Column(INT, ForeignKey("users.id"))
    game_date = Column(TIMESTAMP)
    status = Column(sqlalchemy.Enum(GameStatus), default=GameStatus.PENDING)

    players = relationship("Player", secondary=game_participants_table, back_populates="subscribed_players")

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())



