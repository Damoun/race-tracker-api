"""This file implement the application configuration"""
import os


# pylint: disable=too-few-public-methods
class DefaultConfig(object):
    """This class provide the default configuration"""
    DEBUG = True

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_NAME = "race-tracker-api"
    SECRET_KEY = "PLEASE_CHANGE_ME"

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

    STATIC_DIR = os.path.join(
        PROJECT_ROOT, 'race_tracker_api', 'apps', 'static'
    )
    TEMPLATE_DIR = os.path.join(
        PROJECT_ROOT, 'race_tracker_api', 'apps', 'templates'
    )

    BLUEPRINTS = ()

    LOG_INI = 'etc/logging.ini.json'
