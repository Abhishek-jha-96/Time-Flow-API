from django.utils import timezone

from apps.core.db_layer import db_update_instance
from apps.task.models import Task
from apps.task.settings import Status
from time_flow_api.celery import app

@app.task
def auto_update_task_statuses():
    now = timezone.now()
    tasks = Task.objects.all()

    for task in tasks:
        if task.is_completed:
            new_status = Status.COMPLETED
        elif task.deadline < now:
            new_status = Status.MISSED
        else:
            new_status = Status.UPCOMING

        if task.status != new_status:
            db_update_instance(task, data={"status": new_status})
