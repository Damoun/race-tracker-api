"""
This file provide function to be executed by a worker.
"""
from .models import Race


def send_notification(subscriber, race):
    """
    Send the notification to the subscriber.
    """
    pass


def schedule_race_notification(db, queue, abbrev):
    """
    Retrieve subscribers of a race and schedule notification.
    """
    race = db.query(Race).filter_by(abbrev=abbrev).first()
    for subscriber in race.subscribers:
        queue.enqueue(send_notification, subscriber, race)
