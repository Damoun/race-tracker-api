"""Models for the Users module"""
from datetime import datetime

from race_tracker_api.database import Model
from race_tracker_api.extensions import DB


SUBSCRIPTIONS = DB.Table(
    'subscriptions',
    DB.Column('user_id', DB.Integer, DB.ForeignKey('users.user_id')),
    DB.Column('game_id', DB.Integer, DB.ForeignKey('games.game_id')),
    DB.Column('subscribed_at', DB.DateTime, default=datetime.utcnow)
)


# pylint: disable=too-few-public-methods,no-init
class User(Model):
    """This class describe the SQL schema of an user"""
    __tablename__ = 'users'

    user_id = DB.Column(DB.Integer, primary_key=True, unique=True,
                        nullable=False)
    email = DB.Column(DB.String(255), nullable=False)
    is_active = DB.Column(DB.Boolean, nullable=False, default=False)
    is_admin = DB.Column(DB.Boolean, nullable=False, default=False)
    joined_at = DB.Column(DB.DateTime, default=datetime.utcnow)
    subscriptions = DB.relationship(
        'Game', secondary=SUBSCRIPTIONS,
        backref=DB.backref('subscribers', lazy='dynamic')
    )
