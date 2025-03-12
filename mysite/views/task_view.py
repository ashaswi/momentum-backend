from rest_framework import viewsets
from mysite.models import Task
from mysite.serializers.task_serializer import TaskSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['id']
    ordering = ['-id']
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)