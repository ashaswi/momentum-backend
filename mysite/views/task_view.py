from rest_framework import viewsets
from mysite.models import Task
from rest_framework.filters import OrderingFilter
from mysite.serializers.task_serializer import TaskSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class TaskFilter(filters.FilterSet):
    status = filters.CharFilter(field_name="status", lookup_expr="iexact") 

    class Meta:
        model = Task
        fields = ['status']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    ordering_fields = ['id']
    ordering = ['-id']
    filterset_class = TaskFilter


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  