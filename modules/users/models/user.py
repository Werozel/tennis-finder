from sqlalchemy import Column, INT, VARCHAR, FLOAT, TIMESTAMP, func
from sqlalchemy.orm import relationship

from modules.core.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(INT, primary_key=True)
    full_name = Column(VARCHAR(100), nullable=False)
    login = Column(VARCHAR(50), unique=True, nullable=False)
    password = Column(VARCHAR(512), nullable=False)
    email = Column(VARCHAR(100))
    phone = Column(VARCHAR(12))
    skill = Column(FLOAT, nullable=False)

    wins = Column(INT, default=0)
    losses = Column(INT, default=0)
    cancels = Column(INT, default=0)

    games = relationship("Game", back_populates="players")

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
