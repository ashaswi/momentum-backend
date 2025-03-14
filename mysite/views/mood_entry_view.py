from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from mysite.models import MoodEntry
from mysite.serializers.mood_entry_serializer import MoodEntrySerializer
from rest_framework.filters import OrderingFilter

class MoodEntryViewSet(viewsets.ModelViewSet):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodEntrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['id']
    ordering = ['-id']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)