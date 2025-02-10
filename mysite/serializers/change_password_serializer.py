from rest_framework import serializers
from django.contrib.auth import get_user_model

from mysite.models import PasswordResetCode

User = get_user_model()

class ChangePasswordSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)

    def validate_code(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError("Invalid code format. Must be 6 digits.")
        return value

    def validate(self, data):
        if data["new_password"] != data["confirm_new_password"]:
            raise serializers.ValidationError("Passwords do not match.")

        try:
            reset_code = PasswordResetCode.objects.get(code=data["code"])
        except PasswordResetCode.DoesNotExist:
            raise serializers.ValidationError({"code": "Invalid or expired code."})

        if reset_code.is_expired:
            reset_code.delete()
            raise serializers.ValidationError({"code": "Code has expired."})

        data["reset_code"] = reset_code
        return data