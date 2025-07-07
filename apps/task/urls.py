from rest_framework import routers

from apps.task.settings import TASK_APP
from apps.task.views import TaskViewSet

app_name = TASK_APP

router = routers.DefaultRouter()
router.register("task", TaskViewSet, basename="task")
urlpatterns = router.urls