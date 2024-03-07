from django.contrib.auth.hashers import make_password
from .models import Role, User  
from ninja.errors import ValidationError
from ninja_jwt.tokens import RefreshToken
from .schemas import UserProfileIn

def create_user(email, password):
    if User.objects.filter(email=email).exists():
        raise ValidationError('A user with that email already exists')
    user = User.objects.create(email=email, password=make_password(password))
    return user

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {'refresh': str(refresh), 'access': str(refresh.access_token)}

def update_user_profile(user, payload):
    for attr, value in payload.items():
        if value is not None:
            setattr(user, attr, value)
    user.save()
    return user

def get_user_roles(user):
    return [{'name': role.get_name_display()} for role in user.roles.all()]

def get_all_roles():
    return [{'id': role.id, 'name': role.get_name_display()} for role in Role.objects.all()]