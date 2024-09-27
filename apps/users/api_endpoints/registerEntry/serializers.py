from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegisterModelSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    full_name = serializers.CharField()