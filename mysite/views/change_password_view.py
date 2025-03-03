from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from mysite.models import PasswordResetCode
from mysite.serializers.change_password_serializer import ChangePasswordSerializer
from mysite.serializers.password_reset_request_serializer import PasswordResetRequestSerializer


class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data["code"]
            code_entity = PasswordResetCode.objects.get(code=code)
            user = code_entity.user
            user.set_password(serializer.validated_data["new_password"])
            user.save()

            serializer.validated_data["reset_code"].delete()
            return Response({"message": "Password updated successfully"}, status=200)
        else:
            return Response(serializer.errors, status=400)