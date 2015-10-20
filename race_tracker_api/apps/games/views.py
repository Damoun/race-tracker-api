"""This file provide the resource for the games endpoint"""
from flask import Blueprint
from flask.ext.restful import Resource
from flask.ext.rq import get_queue

from race_tracker_api.extensions import API
from .models import Game
from .jobs import send_notification


GAMES = Blueprint('games', __name__)


# pylint: disable=no-init,too-few-public-methods,no-self-use,no-member
class RaceResource(Resource):
    """This class handle the /races/ endpoint"""

    def post(self, abbrev):
        """Create a new race"""
        game = Game.query.filter_by(abbrev=abbrev)
        queue = get_queue()
        for subscriber in game.subscribers:
            queue.enqueue(send_notification, subscriber, abbrev)
        return 'OK', 201


API.add_resource(RaceResource, '/games/<string:abbrev>/race')
