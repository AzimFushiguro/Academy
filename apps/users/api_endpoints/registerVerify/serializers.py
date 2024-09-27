from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
class UserRegisterVerifySerializer(serializers.Serializer):
    code = serializers.IntegerField()
    phone_number = serializers.CharField()
