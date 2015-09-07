"""
This file provide the API routing.
"""
from .api import create_race, create_game, list_game, get_game
from .api import list_job, get_job


def setup_routing(app):
    """
    Setup the API route.
    """
    app.post('/race', callback=create_race)

    app.post('/game', callback=create_game)
    app.get('/games/', callback=list_game)
    app.get('/game/<game_id>', callback=get_game)

    app.get('/jobs/', callback=list_job)
    app.get('/job/<job_id>', callback=get_job)
