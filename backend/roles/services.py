from users.models import UserRole  

def get_user_roles(user, status):
    roles = [
        {'name': user_role.role.get_name_display()}
        for user_role in user.user_roles.filter(**{status: True})
    ]
    return roles

def update_user_roles(user, requested_role_ids):

    requested_role_ids = set(requested_role_ids)
    existing_role_ids = set()

    # Update existing roles
    for user_role in user.user_roles.prefetch_related('role').all():
        existing_role_ids.add(user_role.role.id)
        user_role.requested = user_role.role_id in requested_role_ids
        user_role.save()

    new_role_ids = requested_role_ids - existing_role_ids

    # Create new roles
    if new_role_ids:
        UserRole.objects.bulk_create([
            UserRole(user=user, role_id=role_id, requested=True)
            for role_id in new_role_ids
        ])