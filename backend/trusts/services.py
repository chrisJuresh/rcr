from users.models import UserTrust, Trust
from django.db import transaction

def update_user_trust(user, trust_id):
    with transaction.atomic():
        UserTrust.objects.filter(user=user, requested=True).exclude(trust_id=trust_id).update(requested=False)
        UserTrust.objects.update_or_create(user=user, trust_id=trust_id, defaults={'requested': True})

def get_user_trusts(user, status, as_string=False):
    user_trusts = user.user_trusts.filter(**{status: True})
    if status == 'requested':
        return user_trusts.first().trust if user_trusts else None
    elif status == 'approved':
        if as_string:
            return [user_trust.trust.name for user_trust in user_trusts if user_trust.trust]
        else:
            return [user_trust.trust for user_trust in user_trusts]

def get_user_trust(user):
    user_trust = user.user_trusts.filter(requested=True, approved=True)
    return user_trust.first().trust if user_trust else None