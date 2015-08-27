"""
This file provide the API of the race-tracker.
"""
from redis import Redis
from rq import Queue
from bottle import route, run, request

import settings
from .jobs import notify_race_subscribers


REDIS = Redis()
QUEUE = Queue(connection=REDIS)


@route('/race', method='POST')
def create_race():
    """
    Register a new starting race.
    """
    abbrev = request.forms.get('abbrev')
    QUEUE.enqueue(notify_race_subscribers, abbrev)
    return {'status': 'ok'}


@route('/game/<abbrev>', method='GET')
def get_game(abbrev):
    """
    Retrieve information of a game.
    """
    return {'status': 'ok', 'result': {'abbrev': abbrev}}


@route('/game', method='POST')
def create_game():
    """
    Register a new game.
    """
    return {'status': 'ok'}


@route('/games/', method='GET')
def list_game():
    """
    List registered game.
    """
    return {'status': 'ok', 'result': []}


@route('/jobs/', method='GET')
def list_job():
    """
    List rq jobs.
    """
    return {'status': 'ok', 'result': QUEUE.job_ids}


@route('/job/<job_id>', method='GET')
def get_job(job_id):
    """
    Retrieve information of a rq job.
    """
    job = QUEUE.fetch_job(job_id)
    if job:
        return {'status': 'ok', 'result': job}
    else:
        return {
            'status': 'error',
            'message': 'Job id does not exist',
            'result': job
        }

run(
    host=settings.API_SETTINGS['host'],
    port=settings.API_SETTINGS['port'],
    debug=settings.DEBUG
)
