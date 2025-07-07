from django.db import models

from apps.core.models import CreatedBy, Timestamps


# Create your models here.
class Task(CreatedBy, Timestamps):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=,
        default=,
    )