"""
This file provide function to be executed by a worker.
"""
from redis import Redis
from rq import Queue


REDIS = Redis()
QUEUE = Queue(connection=REDIS)


def notify_race_subscribers(abbrev):
    """
    Retrieve subscribers of a race and schedule notification
    """
    pass
