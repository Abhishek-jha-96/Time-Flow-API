from django.contrib import admin

from apps.task.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "deadline",
        "is_completed",
        "status",
        "priority",
        "created_by"
    )

admin.site.register(Task, TaskAdmin)