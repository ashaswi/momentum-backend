from rest_framework import viewsets

from mysite.models import MoodEntry
from mysite.serializers.mood_entry_serializer import MoodEntrySerializer


class MoodEntryViewSet(viewsets.ModelViewSet):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodEntrySerializer