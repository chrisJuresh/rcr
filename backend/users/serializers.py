from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import Trust, Role

User = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id','name']

class UserSerializer(serializers.ModelSerializer):
    trust = serializers.PrimaryKeyRelatedField(queryset=Trust.objects.all())
    roles = serializers.PrimaryKeyRelatedField(many=True, queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'trust', 'roles', 'can_be_reviewer', 'can_be_representative', 'can_be_rcr_employee']
        extra_kwargs = {'password': {'write_only': True}, 'can_be_reviewer': {'read_only': True}, 'can_be_representative': {'read_only': True}, 'can_be_rcr_employee': {'read_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

