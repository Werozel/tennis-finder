from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import config

engine = create_engine(config.DB_URL, echo=False)
SessionMaker = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
