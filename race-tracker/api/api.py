"""
This file provide the API of the race-tracker.
"""
from redis import Redis
from rq import Queue
from bottle import Bottle, request
from bottleapi import WebApiError
from bottleapi.jsonapi import json_endpoint

import settings
from .jobs import notify_race_subscribers


REDIS = Redis()
QUEUE = Queue(connection=REDIS)
APP = Bottle()


@json_endpoint
def create_race():
    """
    Register a new starting race.
    """
    abbrev = request.forms.get('abbrev')
    QUEUE.enqueue(notify_race_subscribers, abbrev)


@json_endpoint
def get_game(abbrev):
    """
    Retrieve information of a game.
    """
    return {'abbrev': abbrev}


@json_endpoint
def create_game():
    """
    Register a new game.
    """
    pass


@json_endpoint
def list_game():
    """
    List registered game.
    """
    return []


@json_endpoint
def list_job():
    """
    List rq jobs.
    """
    return QUEUE.job_ids


@json_endpoint
def get_job(job_id):
    """
    Retrieve information of a rq job.
    """
    job = QUEUE.fetch_job(job_id)
    if not job:
        raise WebApiError('Job id (%s) does not exist' % job_id, status=400)
    return job
