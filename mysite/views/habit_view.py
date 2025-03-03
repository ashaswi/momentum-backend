from rest_framework import viewsets
from mysite.models import Habit
from mysite.serializers.habit_serializer import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter



class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['id']
    ordering = ['-id']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Automatically assign user