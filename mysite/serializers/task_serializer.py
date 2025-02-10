from rest_framework import serializers
from mysite.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'date', 'is_completed']