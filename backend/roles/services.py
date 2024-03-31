from users.models import UserRole  
from django.db import transaction

def get_user_roles(user, status):
    roles = [
        user_role.role.get_name_display() for user_role in user.user_roles.filter(**{status: True})
    ]
    return roles

def update_user_roles(user, requested_role_ids):
    with transaction.atomic():
        UserRole.objects.filter(user=user).update(requested=False)
        for role_id in requested_role_ids:
            UserRole.objects.update_or_create(
                user=user, role_id=role_id, defaults={'requested': True})