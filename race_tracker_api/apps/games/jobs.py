"""This file provide jobs functions for the races endpoint"""
from flask.ext.rq import job


@job
def send_notification(subscriber, game):
    """Send the notification to the subscriber"""
    pass
