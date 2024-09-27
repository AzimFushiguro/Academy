from rest_framework import serializers
from apps.users.models import User


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
