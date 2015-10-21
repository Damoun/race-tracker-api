"""Create and initialize flask extensions"""
from flask.ext import sqlalchemy, restful, rq


DB = sqlalchemy.SQLAlchemy()
API = restful.Api()
RQ = rq.RQ()
