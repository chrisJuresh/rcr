from .schemas import JDIn
from .models import JD
from trusts.services import get_user_trust
from specialities.models import ConsultantType
from ninja.files import UploadedFile
from django.db import transaction

def save_jd(request, jd: JDIn, file: UploadedFile, jd_obj=None):
    with transaction.atomic():
        jd_obj = jd_obj or JD()
        jd_obj.file = file
        jd_obj.trust = get_user_trust(request.user)
        jd_obj.consultant_type = ConsultantType.objects.get(name=jd.consultant_type)
        jd_obj.creator = request.user
        jd_obj.save()

        jd_obj.primary_specialities.set(jd.primary_specialities)
        if jd.sub_specialities:
            jd_obj.sub_specialities.set(jd.sub_specialities)
    return jd_obj