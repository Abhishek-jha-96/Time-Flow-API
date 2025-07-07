from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
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
