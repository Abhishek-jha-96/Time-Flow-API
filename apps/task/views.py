from rest_framework import viewsets, filters

from apps.task.settings import PATCH
from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['priority', 'deadline', 'created_ts']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def get_serializer(self, *args, **kwargs):
        if self.request.method == PATCH:
            serializer_class = TaskUpdateSerializer
        else:
            serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)