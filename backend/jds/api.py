from ninja import Router, File
from ninja.errors import HttpError
from ninja.files import UploadedFile
from ninja_jwt.authentication import JWTAuth
from django.utils.dateformat import format
from typing import Optional
from .schemas import JDIn, JDPanel
from .models import JD
from trusts.services import get_user_trust
from .services import save_jd

router = Router()

@router.post("/jd/", auth=JWTAuth())
def create_jd(request, jd: JDIn, file: File[UploadedFile]):
    jd_obj = save_jd(request, jd, file)
    return {"id": jd_obj.id}

@router.put("/jd/{jd_id}/", auth=JWTAuth())
def update_jd(request, jd_id: int, jd: JDIn, file: File[UploadedFile]):
    try: 
        jd_obj = JD.objects.get(id=jd_id, trust=get_user_trust(request.user))
    except JD.DoesNotExist:
        raise HttpError(404, "JD not found")

    jd_obj = save_jd(request, jd, file, jd_obj)
    return {"id": jd_obj.id}

@router.get("/jds/", auth=JWTAuth(), response=JDPanel)
def get_jd_panel(request):
    all_jds = JD.objects.filter(trust=get_user_trust(request.user))
    
    jds = [{
        'id': jd.id,
        'consultant_type': jd.consultant_type.get_name_display(),
        'primary_specialties': [ps.name for ps in jd.primary_specialities.all()],
        'sub_specialties': [ss.name for ss in jd.sub_specialities.all()],
        'date': '2024-03-24 to add'
    } for jd in all_jds]

    return {'jds': jds}