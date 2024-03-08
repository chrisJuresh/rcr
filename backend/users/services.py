from django.contrib.auth.hashers import make_password
from .models import UserRole, User  
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

def extract_role_ids(roles):
    if not isinstance(roles, list):
        return set()
    return {role_dict.get('id') for role_dict in roles if role_dict.get('id')}

def update_existing_user_roles(user, requested_role_ids):
    existing_user_roles = user.user_roles.prefetch_related('role').all()
    existing_role_ids = set()

    for user_role in existing_user_roles:
        role_id = user_role.role.id
        existing_role_ids.add(role_id)

        new_requested_status = role_id in requested_role_ids
        if user_role.requested != new_requested_status:
            user_role.requested = new_requested_status
            user_role.save()

    return existing_role_ids

def add_new_user_roles(user, requested_role_ids, existing_role_ids):
    new_role_ids = requested_role_ids - existing_role_ids
    UserRole.objects.bulk_create([
        UserRole(user=user, role_id=role_id, requested=True) for role_id in new_role_ids
    ])

def update_user_roles(user, roles):
    requested_role_ids = extract_role_ids(roles)
    existing_role_ids = update_existing_user_roles(user, requested_role_ids)
    add_new_user_roles(user, requested_role_ids, existing_role_ids)

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
    user_roles = UserRole.objects.filter(user=user, requested=True)
    requested_roles = [{'name': user_role.role.get_name_display()} for user_role in user_roles]
    return requested_roles

def get_approved_roles(user):
    user_roles = UserRole.objects.filter(user=user, approved=True)
    approved_roles = [{'name': user_role.role.get_name_display()} for user_role in user_roles]
    return approved_roles
    