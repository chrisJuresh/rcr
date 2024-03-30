from users.models import UserRole  

def get_user_roles(user, status):
    roles = [
        {'name': user_role.role.get_name_display()}
        for user_role in user.user_roles.filter(**{status: True})
    ]
    return roles

def update_user_roles(user, requested_role_ids):
    existing_roles = {role.role_id for role in user.user_roles.prefetch_related('role').all()}
    requested_role_ids = set(requested_role_ids)

    # Identify new roles and update existing ones
    new_role_ids = requested_role_ids - existing_roles
    for user_role in user.user_roles.all():
        is_requested = user_role.role_id in requested_role_ids
        if user_role.requested != is_requested:
            user_role.requested = is_requested
            user_role.save()

    # Bulk create new roles
    if new_role_ids:
        UserRole.objects.bulk_create([
            UserRole(
            user=user, 
            role_id=role_id, 
            requested=True
            ) for role_id in new_role_ids
        ])