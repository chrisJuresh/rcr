from .models import Trust

def update_user_trust(user, trust_id):
    user.trust = Trust.objects.get(id=trust_id)
    user.save()