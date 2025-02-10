from rest_framework import viewsets
from mysite.models import Task
from mysite.serializers.task_serializer import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 