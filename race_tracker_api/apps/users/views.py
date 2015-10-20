"""This file provide the resource for the users endpoint"""
from flask import Blueprint
from flask.ext.restful import Resource, fields, marshal_with

from race_tracker_api.extensions import API
from .models import User


USERS = Blueprint('users', __name__)


# pylint: disable=no-init,too-few-public-methods,no-self-use,no-member
class UserResource(Resource):
    """This class handle the /users/<user_id> endpoint"""

    game_fields = {
        'abbrev': fields.String,
        'subscribed_at': fields.DateTime(dt_format='iso8601')
    }

    user_fields = {
        'user_id': fields.Integer,
        'email': fields.String,
        'is_active': fields.Boolean,
        'is_admin': fields.Boolean,
        'joined_at': fields.DateTime(dt_format='iso8601'),
        'subscriptions': fields.List(fields.Nested(game_fields))
    }

    @marshal_with(user_fields)
    def get(self, user_id):
        """Retrieve an user"""
        return User.query.get_or_404(user_id)


API.add_resource(UserResource, '/users/<int:user_id>')
