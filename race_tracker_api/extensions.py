"""Create and initialize flask extensions"""
from flask.ext import sqlalchemy, restful, rq, log
from flask_oauthlib.client import OAuth


DB = sqlalchemy.SQLAlchemy()
API = restful.Api()
RQ = rq.RQ()
LOGGER = log.Logging()
OAUTH = OAuth()
