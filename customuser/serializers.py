from rest_framework import serializers
from .models import custom_users

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = custom_users
        fields = ["id", "email", "uname", "password"]