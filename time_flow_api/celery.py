import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "time_flow_api.settings"
)

app = Celery("time_flow_api")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'task_status_clean_up': {
        'task': 'apps.task.tasks.auto_update_task_statuses',
        'schedule': crontab(minute='*/15'),
    }
}

app.autodiscover_tasks()
