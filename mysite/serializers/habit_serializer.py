from rest_framework import serializers
from mysite.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['name','start_date','start_time','created_at']