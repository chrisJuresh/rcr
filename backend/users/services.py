from django.contrib.auth.hashers import make_password
from .models import UserRole, User, Trust, UnauthenticatedUser
from ninja.errors import ValidationError
from ninja_jwt.tokens import RefreshToken
from .schemas import UserProfileIn
from django.shortcuts import get_object_or_404
from django.db import transaction

def user_exists(email):
    return User.objects.filter(email=email).exists()

def create_user(email, password):
    user = User.objects.create(email=email, password=password)
    return user

def create_unauthenticated_user(user):
    UnauthenticatedUser.objects.create(email=user.email, password=make_password(user.password), token=user.token)

def get_token_for_user(user):
    return RefreshToken.for_user(user)

def register_user(unauth_user, token):
    with transaction.atomic():
        user = create_user(unauth_user.email, unauth_user.password)
        unauth_user.delete()
        tokens = get_token_for_user(user)
        return {
            'message': 'User registered successfully',
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        }

def get_user_roles(user):
    return [{'name': role.role.get_name_display()} for role in user.user_roles.filter(requested=True)]

def get_user_approved_roles(user):
    return [{'name': role.role.get_name_display()} for role in user.user_roles.filter(approved=True)]

def get_user_profile(user):
    return {
        "email": user.email,
        "title": user.title,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "trust": user.trust.name if user.trust else None,
        "roles": get_user_roles(user),
        "approved_roles": get_user_approved_roles(user)
    }

def update_user_roles(user, requested_role_ids):

    requested_role_ids = set(requested_role_ids)

    existing_role_ids = set()

    for user_role in user.user_roles.prefetch_related('role').all():
        role_id = user_role.role.id
        existing_role_ids.add(role_id)
        user_role.requested = role_id in requested_role_ids
        user_role.save()

    new_role_ids = requested_role_ids - existing_role_ids
    if new_role_ids:
        UserRole.objects.bulk_create([
            UserRole(user=user, role_id=role_id, requested=True)
            for role_id in new_role_ids
        ])

def update_user_trust(user, trust_id):
    user.trust = Trust.objects.get(id=trust_id)
    user.save()

def update_user_attribute(user, attr, value):
    if value is None:
        return
    if attr == 'roles':
        update_user_roles(user, value)
    elif attr == 'trust':
        update_user_trust(user, value)
    else:
        setattr(user, attr, value)

def update_user_profile(user, payload):
    payload_dict = payload.dict()
    for attr, value in payload_dict.items():
        update_user_attribute(user, attr, value)
    user.save()
    return user


    