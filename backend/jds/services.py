from .schemas import JDIn
from .models import JD
from trusts.services import get_user_trust, get_user_trusts
from roles.services import get_user_roles
from specialities.models import ConsultantType
from ninja.files import UploadedFile
from django.db import transaction
from django.db.models import Q


def save_jd(request, file: UploadedFile, jd=None, jd_obj=None):
    if jd is None:
        with transaction.atomic():
            jd_obj = jd_obj or JD()
            jd_obj.file = file
            jd_obj.save()

        return jd_obj

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

def user_jds(user, panel=None):
    roles = get_user_roles(user, ['approved', 'requested'])
    trust = get_user_trust(user)
    approved_trusts = get_user_trusts(user, 'approved')
    jds = JD.objects.none()

    if 'Trust Employee' in roles and panel=='Edit':
        jds = JD.objects.filter(trust=trust, status__in=['Draft', 'RSA Rejected'])
        return jds

    if 'Trust Employee' in roles and panel=='AAC':
        jds = JD.objects.filter(trust=trust, status='RSA Approved')
        return jds
    
    if 'RCR Employee' in roles and panel=='Review':
        jds = JD.objects.filter(status='Trust Submitted')
        return jds

    if 'Reviewer' in roles and panel=='Review':
        jds = JD.objects.filter(
            ~Q(trust__in=approved_trusts) &
            Q(consultant_type=user.user_specialities.consultant_type) & (
            Q(status='RCR Approved') |
            Q(status='Trust Amended') )
        )
        return jds

    if 'Trust Employee' in roles:
        jds |= JD.objects.filter(trust=trust)
    if 'RCR Employee' in roles:
        jds |= JD.objects.all()
    if 'Reviewer' in roles:
        jds |= JD.objects.filter(
            ~Q(trust__in=approved_trusts) &
            Q(consultant_type=user.user_specialities.consultant_type) & (
            Q(status='RCR Approved') |
            Q(status='Trust Amended') |
            Q(status='RSA Rejected') |
            Q(status='RSA Approved') )
        )
    return jds