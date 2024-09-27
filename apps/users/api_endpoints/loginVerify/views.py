
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginVerifySerializer
from apps.users.models import User
from django.core.cache import cache
import random
from apps.users.utils import get_tokens_for_user

class LoginVerifyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginVerifySerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get("phone_number")
            code = serializer.data.get("code")
            cache_key = f"otp_{phone_number}"
            cache_code = cache.get(cache_key)
            if cache_code is None:
                return Response({
                    "success": False, "errors": "Your OTP is expired"
                })
            if code != cache_code:
                return Response({
                    "success": False, "errors": "You have entered wrong OTP"
                })
            user = User.objects.get(phone_number=phone_number)
            tokens=  get_tokens_for_user(user)
            return Response(tokens)
        return Response({"success": False, "errors": serializer.errors})
