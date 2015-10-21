"""This file create and configure the Flask application"""
import logging
import json
import os

from flask import Flask

from config import DefaultConfig
from .helpers import load_module_instances


def get_app(config=None, **kwargs):
    """Creates a Flask application"""
    app = Flask(__name__, **kwargs)

    configure_app(app, config)

    configure_extensions(app)
    configure_blueprints(app)
    configure_logging(app)

    return app


def configure_app(app, config):
    """Configure the application"""
    app.config.from_object(DefaultConfig)

    if config is not None:
        app.config_from_object(config)

    if 'CONFIG_ENV' in app.config and app.config['CONFIG_ENV'] in os.environ:
        app.config.from_envvar(app.config['CONFIG_ENV'])


def configure_blueprints(app):
    """Setup the blueprints"""
    blueprints = app.config['BLUEPRINTS'] if 'BLUEPRINTS' in app.config else []
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_extensions(app):
    """Setup the extensions"""
    for ext in load_module_instances('.extensions',
                                     package="race_tracker_api"):
        if getattr(ext, 'init_app', False):
            ext.init_app(app)


def configure_logging(app):
    """Configure logging"""
    log_ini = os.path.join(app.root_path, app.config['LOG_INI'])

    if os.path.exists(log_ini):
        with open(log_ini, 'rt') as handle:
            log_config = json.load(handle)
        logging.config.dictConfig(log_config)
