from users.models import UserTrust, Trust
from django.db import transaction

def update_user_trust(user, trust_id):
    trust = Trust.objects.get(id=trust_id)

    with transaction.atomic():
        # Set all other trusts to requested = False
        UserTrust.objects.filter(user=user, requested=True).exclude(trust=trust).update(requested=False)

        # Get or create the UserTrust instance
        user_trust, created = UserTrust.objects.get_or_create(
            user=user,
            trust=trust,
            defaults={'requested': True}
        )

        # If the UserTrust instance already exists, set requested = True
        if not created:
            user_trust.requested = True
            user_trust.save(update_fields=['requested'])

def get_user_trusts(user, status):
    if status == 'requested':
        user_trust = user.user_trusts.filter(requested=True).first()
        trusts = user_trust.trust.name if user_trust else None
    elif status == 'approved':
        trusts = [
            {'name': user_trust.trust.name} 
            for user_trust in user.user_trusts.filter(approved=True)]

    return trusts

def get_user_trust(user):
    user_trust = UserTrust.objects.filter(user=user, requested=True, approved=True).first()
    return user_trust.trust if user_trust else None