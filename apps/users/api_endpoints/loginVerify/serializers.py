from rest_framework import serializers
from apps.users.models import User


class UserLoginVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.IntegerField()