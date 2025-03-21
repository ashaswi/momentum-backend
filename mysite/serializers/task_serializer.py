from rest_framework import serializers
from mysite.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name','start_date','created_at','status']