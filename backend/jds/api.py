from ninja import Router, File
from ninja.errors import HttpError
from ninja.files import UploadedFile
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from django.utils.dateformat import DateFormat  

from .schemas import JDIn, JDPanel
from .models import JD
from specialities.models import ConsultantType, Speciality

router = Router()

@router.post("/jd/", auth=JWTAuth())
def create_jd(request, jd: JDIn, file: File[UploadedFile]):
    trust = request.user.trust
    consultant_type = ConsultantType.objects.get(name=jd.consultant_type)
    creator = request.user

    jd_instance = JD(
        file=file,
        trust=trust,
        consultant_type=consultant_type,
        creator=creator
    )
    jd_instance.save()
    
    jd_instance.primary_specialities.set(Speciality.objects.filter(id__in=jd.primary_specialities))
    if jd.sub_specialities:
        jd_instance.sub_specialities.set(Speciality.objects.filter(id__in=jd.sub_specialities))

    return {"id": jd_instance.id}

@router.put("/jd/{jd_id}/", auth=JWTAuth())
def update_jd(request, jd_id: int, jd: JDIn, file: File[UploadedFile]):
    trust = request.user.trust
    try:
        jd_instance = JD.objects.get(id=jd_id, trust=trust)
    except JD.DoesNotExist:
        return {"error": "JD with the provided ID does not exist."}

    consultant_type = ConsultantType.objects.get(name=jd.consultant_type)
    
    jd_instance.file = file
    jd_instance.consultant_type = consultant_type
    jd_instance.save()
    
    jd_instance.primary_specialities.set(Speciality.objects.filter(id__in=jd.primary_specialities))
    if jd.sub_specialities:
        jd_instance.sub_specialities.set(Speciality.objects.filter(id__in=jd.sub_specialities))

    return {"id": jd_instance.id}

@router.get("/jds/", auth=JWTAuth(), response=JDPanel)
def get_jd_panel(request):
    all_jds = JD.objects.filter(trust=request.user.trust)
    jds = []

    for jd in all_jds:
        primary_specialties = [ps.name for ps in jd.primary_specialities.all()]
        sub_specialties = [ss.name for ss in jd.sub_specialities.all()]

        latest_edit_date = jd.history.first().history_date if jd.history.exists() else jd.submission_date
        latest_edit_date_str = DateFormat(latest_edit_date).format('Y-m-d H:i:s')  
 
        jds.append({
            'id': jd.id,
            'consultant_type': jd.consultant_type.get_name_display(),
            'primary_specialties': primary_specialties,
            'sub_specialties': sub_specialties,
            'date': latest_edit_date_str 
        })

    return {'jds': jds}
