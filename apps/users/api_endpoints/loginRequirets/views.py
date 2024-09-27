from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer
from apps.users.models import User
from django.core.cache import cache
import random
from apps.users.utils import generator_random_6_digits


class LoginRequestAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get("phone_number")
            cache_key = f"otp_{phone_number}"
            if cache.get(cache_key):
                return Response(
                    {"success": False, "errors": "We have already sent an SMS. Try again in 60 seconds."}
                )
            if not User.objects.filter(phone_number=phone_number, is_verified = True ).exists():
                return Response(
                    {"success": False, "error": "User not found."}
                )
            code = generator_random_6_digits()
            cache.set(cache_key, code, 60)
            print(f"Generated OTP: {code} for phone number: {phone_number}")
            return Response({"success": True, "message": "We have sent an SMS."})
        return Response({"success": False, "errors": serializer.errors})
