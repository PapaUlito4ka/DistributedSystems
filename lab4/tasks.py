from time import sleep

from celery import shared_task

from datetime import datetime


@shared_task
def large_task(message: str):
    sleep(5)
    print(f'Received {message} at {datetime.now()}')
