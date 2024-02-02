from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Trust
from django.contrib.auth import authenticate

User = get_user_model()

class TrustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trust
        fields = ['id','name']

class UserSerializer(serializers.ModelSerializer):
    trust = serializers.PrimaryKeyRelatedField(queryset=Trust.objects.all())

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'trust']
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")