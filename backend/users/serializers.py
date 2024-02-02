from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Trust

User = get_user_model()

class TrustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trust
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    trust = TrustSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'trust']
        extra_kwargs = {'password': {'write_only': True}}