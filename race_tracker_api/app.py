"""This file create and configure the Flask application"""
import logging
import json
import os

from flask import Flask, jsonify, render_template, request

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


# pylint: disable=unused-variable
def configure_error_handlers(app):
    """Configure errors pages"""
    @app.errorhandler(401)
    def unauthorized(error):
        """Error handler on unauthorized request"""
        if request.is_xhr:
            return jsonify(error="Unauthorized")
        return render_template("errors/unauthorized.html", error=error), 401

    @app.errorhandler(404)
    def not_found(error):
        """Error handler on resource not found"""
        if request.is_xhr:
            return jsonify(error="Page not found")
        return render_template("errors/not_found.html", error=error), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        """Error handler on internal server error"""
        if request.is_xhr:
            return jsonify(error="An error has occurred")
        return render_template("errors/internal_server_error.html",
                               error=error), 500


def configure_logging(app):
    """Configure logging"""
    log_ini = os.path.join(app.root_path, app.config['LOG_INI'])

    if os.path.exists(log_ini):
        with open(log_ini, 'rt') as handle:
            log_config = json.load(handle)
        logging.config.dictConfig(log_config)
