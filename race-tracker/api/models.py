"""
This file describe the database schema.
"""
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from settings import settings

Base = declarative_base()
engine = create_engine(settings.get('sql', 'url'), echo=True)
plugin = sqlalchemy.Plugin(
    engine, Base.metadata, create=True, commit=True, use_kwargs=True
)


class Subscriber(Base):
    """
    This class represent a subscriber.
    """
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    race_id = Column(Integer, ForeignKey('races.id'))
    races = relationship("Race")

    def __init__(self):
        pass


class Game(Base):
    """
    This class represent a game.
    """
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    races = relationship("Race")

    def __init__(self, name):
        self.name = name


class Race(Base):
    """
    This class represent a race.
    """
    __tablename__ = "races"

    id = Column(Integer, primary_key=True)
    abbrev = Column(String, nullable=False, unique=True)
    game_id = Column(Integer, ForeignKey('games.id'))

    def __init__(self, abbrev, game_id):
        self.abbrev = abbrev
        self.game_id = game_id
