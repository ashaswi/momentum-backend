from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mysite.models import PasswordResetCode
from mysite.serializers.password_reset_request_serializer import PasswordResetRequestSerializer

class GenerateResetCodeView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

            reset_code = get_random_string(length=6, allowed_chars="0123456789")

            PasswordResetCode.objects.create(user=user, code=reset_code)

            send_mail(
                subject="Your Password Reset Code",
                message=f"Your password reset code is: {reset_code}",
                from_email="mail@momentum.com",
                recipient_list=[email],
            )

            return Response({"message": "Password reset code sent to your email"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)