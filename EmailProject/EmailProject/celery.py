from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmailProject.settings')

app = Celery('EmailProject')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings,namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-first-day-of-every-month':{
        'task':'send_mail.tasks.send_mail_func',
        'schedule': crontab(
            day_of_month=1,
            hour=10,
            minute=0
            ),
        # 'args':(2)
    }
}

app.autodiscover_tasks()
@app.task(bind=True)

def debug_task(self):
    print(f'Request:{self.request!r}')
