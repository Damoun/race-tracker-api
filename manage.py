#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate
from flask.ext.migrate import MigrateCommand

from race_tracker_api.app import get_app
from race_tracker_api.extensions import DB

APP = get_app()

# initialize flask-migrate
MIGRATE = Migrate(APP, DB)

MANAGER = Manager(APP)
MANAGER.add_command('db', MigrateCommand)


@MANAGER.command
def createdb():
    """
    Creates all database tables
    """
    DB.create_all()


@MANAGER.command
def dropdb():
    """
    Drops all database tables
    """
    if prompt_bool("Are you sure you want to lose all your data"):
        DB.drop_all()


if __name__ == "__main__":
    MANAGER.run()
