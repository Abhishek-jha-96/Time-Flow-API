from django.db import models

from apps.core.models import CreatedBy, Timestamps
from apps.task.settings import (
    PRIORITY_MAX_LEN, 
    STATUS_MAX_LEN, 
    TITLE_MAX_LEN, 
    Priority, 
    Status
)


# Create your models here.
class Task(CreatedBy, Timestamps):
    """
    Model For Task.
    """
    title = models.CharField(max_length=TITLE_MAX_LEN)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=Status.choices,
        default=Status.UPCOMING,
    )
    priority = models.CharField(
        max_length=PRIORITY_MAX_LEN,
        choices=Priority.choices,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title