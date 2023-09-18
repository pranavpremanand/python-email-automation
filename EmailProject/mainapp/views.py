from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse
from send_mail.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse('Done')

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse('Sent')

def schedule_mail(request):
    schedule,created = CrontabSchedule.objects.get_or_create(hour=14,minute=29)
    task = PeriodicTask.objects.create(crontab=schedule,name='schedule_mail_task_'+'6',
                                       task='send_mail.tasks.send_mail_func')
    return HttpResponse('Done')