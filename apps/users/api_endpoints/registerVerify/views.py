from email.policy import default
from lib2to3.btm_utils import tokens

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterVerifySerializer
from apps.users.models import User
from django.core.cache import cache
from apps.users.utils import generator_random_6_digits, get_tokens_for_user
from django.core.exceptions import ValidationError


class RegisterVerifyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterVerifySerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get("phone_number")
            code = serializer.validated_data.get("code")

            if User.objects.filter(phone_number=phone_number, is_verified=True).exists():
                raise ValidationError({"success": False, "errors": "PhoneNumber is Already taken"})

            if not User.objects.filter(phone_number=phone_number, is_verified=False).exists():
                raise ValidationError({"success": False, "errors": "Can't find not verified number"})

            cache_key = f"otp_register_{phone_number}"
            cached_key = cache.get(cache_key)
            if cached_key is None:
                return Response({"success": False, "message": "Your otp is expired"}, status=400)

            if cached_key != code:
                return Response({"success": False, "message": "Wrong OTP"}, status=400)
            user = User.objects.get(phone_number=phone_number, is_verified=False)
            user.is_verified = True
            user.save()

            tokens = get_tokens_for_user(user)
            cache.set(cache_key, code, 60)
            return Response(tokens)

        return Response({"success": False, "errors": serializer.errors})
