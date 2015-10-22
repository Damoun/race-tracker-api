"""Create and initialize flask extensions"""
from flask.ext import sqlalchemy, restful, rq, log


DB = sqlalchemy.SQLAlchemy()
API = restful.Api()
RQ = rq.RQ()
LOGGER = log.Logging()
