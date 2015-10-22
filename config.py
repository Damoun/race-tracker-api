"""This file implement the application configuration"""
import os

from race_tracker_api.apps.users import USERS
from race_tracker_api.apps.games import GAMES


# pylint: disable=too-few-public-methods
class DefaultConfig(object):
    """This class provide the default configuration"""
    DEBUG = True
    FLASK_LOG_LEVEL = 'DEBUG'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_NAME = "race-tracker-api"
    SECRET_KEY = "PLEASE_CHANGE_ME"

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

    BLUEPRINTS = (USERS, GAMES)
