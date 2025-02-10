from django.contrib.auth.models import User
from rest_framework import serializers


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self,value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email not found.")
        return value