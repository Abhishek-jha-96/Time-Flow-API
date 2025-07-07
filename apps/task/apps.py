from django.apps import AppConfig

from apps.task.settings import TASK_APP


class TaskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = TASK_APP
