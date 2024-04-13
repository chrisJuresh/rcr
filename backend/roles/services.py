from users.models import UserRole  
from django.db import transaction

def get_user_roles(user, status):
    status_list = status if isinstance(status, list) else [status]
    query = {f"{stat}": True for stat in status_list}

    roles = [
        user_role.role.get_name_display()
        for user_role in user.user_roles.filter(**query)
    ]
    
    return roles

def update_user_roles(user, requested_role_ids):
    with transaction.atomic():
        UserRole.objects.filter(user=user).update(requested=False)
        for role_id in requested_role_ids:
            UserRole.objects.update_or_create(
                user=user, role_id=role_id, defaults={'requested': True})