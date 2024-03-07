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
    token = RefreshToken.for_user(user)
    return token


def update_user_roles(user, roles):
    if not isinstance(roles, list):
        return
    role_ids = [role_dict.get('id') for role_dict in roles]
    role_ids = list(filter(None, role_ids))
    if role_ids:
        user.roles.set(role_ids)


def update_user_attribute(user, attr, value):
    if value is None:
        return
    if attr == 'roles':
        update_user_roles(user, value)
    else:
        setattr(user, attr, value)


def update_user_profile(user, payload):
    payload_dict = payload.dict()
    for attr, value in payload_dict.items():
        update_user_attribute(user, attr, value)
    user.save()
    return user


def get_user_roles(user):
    return [{'name': role.get_name_display()} for role in user.roles.all()]
