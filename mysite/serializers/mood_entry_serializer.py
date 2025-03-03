from rest_framework import serializers
from mysite.models import  MoodEntry


class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = ['feeling', 'content', 'created_at']