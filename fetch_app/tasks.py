from celery import shared_task

from .fetch import fetch_13f_filings




@shared_task(name="fetch_filings")
def fetch_filings():

    print("started ...........")
    return fetch_13f_filings()