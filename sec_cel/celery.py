import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','sec_cel.settings')

app = Celery('sec_cel')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()