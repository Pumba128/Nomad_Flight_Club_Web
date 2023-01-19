from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nomad_flight_club.settings')

app = Celery('nomad_flight_club')
app.conf.enable_utc = False
app.conf.update(timezone = 'Europe/Warsaw')
app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings here
app.conf.beat_schedule = {
    'update-flight-details-every-hour': {
        'task': 'web.tasks.flight_details_update_celery',
        'schedule': crontab(hour='*')
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

