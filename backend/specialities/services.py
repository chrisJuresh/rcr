from .models import Speciality, ConsultantType
from users.models import UserSpecialities

def get_user_consultant_type(user):
    try:
        return user.user_specialities.consultant_type.get_name_display()
    except:
        return None

def get_user_specialities(user):
    try:
        speciality_ids = user.user_specialities.specialities.values_list('id', flat=True)
        consultant_type = user.user_specialities.consultant_type
        specialities = Speciality.objects.filter(
            id__in=speciality_ids,
            consultant_type=consultant_type
        )
        specialities = [
            {
                'id': speciality.id,
                'name': speciality.name,
            } for speciality in specialities
        ]
        return specialities
    except:
        return None

def get_or_create_user_specialities(user):
    return UserSpecialities.objects.get_or_create(user=user, defaults={'user': user})

def update_user_specialities(user, specialities_ids):
    specialities = Speciality.objects.filter(id__in=specialities_ids)
    user_specialities, _ = get_or_create_user_specialities(user)
    user_specialities.specialities.set(specialities)
    user_specialities.save()

def update_user_consultant_type(user, consultant_type_name):
    consultant_type = ConsultantType.objects.get(name=consultant_type_name.upper())
    user_specialities, _ = get_or_create_user_specialities(user)
    user_specialities.consultant_type = consultant_type
    user_specialities.save()