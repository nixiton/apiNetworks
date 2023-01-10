from django.core.mail import send_mail

from stats import celery_app

from stats import settings

@celery_app.task()
def send_mail_task():
    pass