"""Models for the Games module"""
from race_tracker_api.database import Model
from race_tracker_api.extensions import DB


# pylint: disable=too-few-public-methods,no-init
class Game(Model):
    """This class describe the SQL schema of a game"""
    __tablename__ = 'games'

    game_id = DB.Column(DB.Integer, primary_key=True, unique=True,
                        nullable=False)
    name = DB.Column(DB.String(254), nullable=False)
    abbrev = DB.Column(DB.String(50), unique=True, nullable=False)
