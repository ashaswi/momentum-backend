from rest_framework import serializers
from mysite.models import Journal


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['title', 'content','created_at']