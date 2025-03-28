from rest_framework import serializers
from mysite.models import Task

class TaskSerializer(serializers.ModelSerializer):
    description= serializers.CharField(required=False,allow_null=True,allow_blank=True)
    class Meta:
        model = Task
        fields = ['id','name','start_date','description','created_at','status']