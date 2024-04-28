from ninja import Router, Schema
from datetime import date
from typing import List, Optional
from jds.models import JD
from .models import AAC
from specialities.models import ConsultantType
from ninja_jwt.authentication import JWTAuth
import json
from trusts.services import get_user_trust
from ninja.errors import HttpError

router = Router()

class AACIn(Schema):
    trust: int
    consultant_type: str
    JDs: str
    date: str

class PanelAAC(Schema):
    id: int
    status: str
    date: str
    consultant_type: str
    primary_specialties: List[str]
    sub_specialties: Optional[List[str]]

class AACPanel(Schema):
    aacs: List[PanelAAC]

class AACIDsOut(Schema):
    ids: List[int]

class JDforAAC(Schema):
    id: int
    file: str
    primary_specialities: List[str]
    sub_specialities: List[str]

class AACOut(Schema):
    id: int
    date: str
    trust: str
    consultant_type: str
    status: str
    jds: List[JDforAAC]

@router.post("/aac/", auth=JWTAuth())
def create_aac(request, aac: AACIn):
    try:
        jd_ids = json.loads(aac.JDs)  
    except json.JSONDecodeError as e:
        raise HttpError(400, "Invalid JSON string for 'jds' field")
    
    jds = JD.objects.filter(id__in=jd_ids)
    aac_instance = AAC.objects.create(
        trust_id=aac.trust,
        consultant_type = ConsultantType.objects.get(name=aac.consultant_type.upper()),
        date=aac.date
    )
    aac_instance.jds.set(jds)

@router.get("/panel/", auth=JWTAuth(), response=AACPanel)
def get_aac_panel(request):
    all_aacs = AAC.objects.filter(trust=get_user_trust(request.auth)).prefetch_related(
        'jds__primary_specialities',
        'jds__sub_specialities'
    )

    aacs = [{
        'id': aac.id,
        'date': aac.date.strftime('%Y-%m-%d') if aac.date else None,
        'consultant_type': aac.consultant_type.get_name_display(),
        'status': 'Submitted',
        'primary_specialties': list(set(
            specialty.name
            for jd in aac.jds.all()
            for specialty in jd.primary_specialities.all()
        )),
        'sub_specialties': (lambda subs: subs if subs else [""])(list(set(
            specialty.name
            for jd in aac.jds.all()
            for specialty in jd.sub_specialities.all()
        )))
    } for aac in all_aacs]

    return {'aacs': aacs}

@router.get("/ids/", auth=JWTAuth(), response=AACIDsOut)
def get_aac_ids(request):
    aacs = AAC.objects.filter(trust=get_user_trust(request.auth))
    return {"ids": [aac.id for aac in aacs]}

@router.get("/{aac_id}/", auth=JWTAuth(), response=AACOut)
def get_aac(request, aac_id: int):
    try:
        aac = AAC.objects.get(id=aac_id, trust=get_user_trust(request.auth))
    except AAC.DoesNotExist:
        raise HttpError(404, "AAC not found")

    return {
        'id': aac.id,
        'date': aac.date.strftime('%Y-%m-%d') if aac.date else None,
        'trust': aac.trust.name,
        'consultant_type': aac.consultant_type.get_name_display(),
        'status': 'Submitted',
        'jds': [{
            'id': jd.id,
            'file': jd.file,
            'primary_specialities': [ps.name for ps in jd.primary_specialities.all()],
            'sub_specialities': [ss.name for ss in jd.sub_specialities.all()]
        } for jd in aac.jds.all()]
    }

@router.put("/{aac_id}/{rep_id}/", auth=JWTAuth())
def update_aac_rep(request, aac_id: int, rep_id: int):
    try:
        aac = AAC.objects.get(id=aac_id, trust=get_user_trust(request.auth))
    except AAC.DoesNotExist:
        raise HttpError(404, "AAC not found")

    aac.representative_id = rep_id
    aac.save()