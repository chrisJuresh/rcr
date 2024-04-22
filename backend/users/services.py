from django.contrib.auth.hashers import make_password
from .models import User, UnauthenticatedUser
from ninja_jwt.tokens import RefreshToken
from django.db import transaction
from roles.services import get_user_roles, update_user_roles
from trusts.services import update_user_trust, get_user_trusts
from specialities.services import update_user_specialities, update_user_consultant_type, get_user_specialities, get_user_consultant_type
from django.db.models import Q

def user_exists(email):
    return User.objects.filter(email=email).exists()

def create_user(email, password):
    user = User.objects.create(email=email, password=password)
    return user

def create_unauthenticated_user(user):
    UnauthenticatedUser.objects.create(
        email=user.email, 
        password=make_password(user.password), 
        token=user.token
    )

def get_tokens_for_user(user):
    tokens = RefreshToken.for_user(user)
    return {
            'message': 'User registered successfully',
            'refresh': str(tokens),
            'access': str(tokens.access_token),
    }

def register_user(unauth_user, token):
    with transaction.atomic():
        user = create_user(unauth_user.email, unauth_user.password)
        unauth_user.delete()
        return user

def get_user_profile(user):
    return {
        "email": user.email,
        "title": user.title,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "trust": get_user_trusts(user, 'requested', as_string=True),
        "approved_trusts": get_user_trusts(user, 'approved', as_string=True),
        "roles": get_user_roles(user, 'requested'),
        "approved_roles": get_user_roles(user, 'approved'),
        "consultant_type": get_user_consultant_type(user),
        "specialities": get_user_specialities(user),
        "updated": user.updated.strftime('%y-%m-%d %H:%M') if user.updated else ""
    }

def update_user_attributes(user, attr, value):
    if value is None:
        return

    attr_handlers = {
        'roles': update_user_roles,
        'trust': update_user_trust,
        'specialities': update_user_specialities,
        'consultant_type': update_user_consultant_type,
    }

    handler = attr_handlers.get(attr)
    if handler:
        handler(user, value)
    else:
        setattr(user, attr, value)

def update_user_profile(user, payload):
    for attr, value in payload.dict().items():
        update_user_attributes(user, attr, value)
    user.save()

def get_jd_reviewers(jd):
    valid_reviewers = []

    reviewers = User.objects.all()

    for reviewer in reviewers:
        try:
            trusts = get_user_trusts(reviewer, 'approved')
            roles = get_user_roles(reviewer, 'approved')
            consultant_type = reviewer.user_specialities.consultant_type
            if jd.trust not in trusts and 'Reviewer' in roles and consultant_type == jd.consultant_type:
                valid_reviewers.append(reviewer)
        except:
            pass
    return valid_reviewers
    