import os
from celery import Celery

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 
    'stats.settings'
)

#BROKER_URL = "redis://:password@127.0.0.1:6379/0"

app = Celery('stats',)#  BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()