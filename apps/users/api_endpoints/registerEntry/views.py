from email.policy import default

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterModelSerializer
from apps.users.models import User
from django.core.cache import cache
from apps.users.utils import generator_random_6_digits
from django.core.exceptions import ValidationError


class RegisterEntryAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterModelSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get("phone_number")
            full_name = serializer.validated_data.get("full_name")

            if User.objects.filter(phone_number=phone_number, is_verified=True).exists():
                raise ValidationError({"success": False, "errors": "PhoneNumber is Already taken"})

            code = generator_random_6_digits()
            cache_key = f"otp_register_{phone_number}"

            if cache.get(cache_key) is not None:
                return Response({"success": False, "message": "We have already sent sms try again in 60 sec "})


            User.objects.update_or_create(
                phone_number=phone_number,
                defaults = {
                    "full_name":full_name
                }
            )
            cache.set(cache_key, code, 60)
            return Response({"success": True, "message": "We have sent an SMS."})

        return Response({"success":False, "errors":serializer.errors})
