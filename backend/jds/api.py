from ninja import Router, File
from ninja.errors import HttpError
from ninja.files import UploadedFile
from ninja_jwt.authentication import JWTAuth
from django.utils.dateformat import format
from typing import Optional
from .schemas import JDIn, JDPanel, JDOut, JDIDsOut, JDID
from .models import JD
from trusts.services import get_user_trust
from .services import save_jd

router = Router()

@router.post("/jd/", auth=JWTAuth(), response=JDID)
def create_jd(request, jd: JDIn, file: File[UploadedFile]):
    jd_obj = save_jd(request, jd, file)
    return {"id": jd_obj.id}

@router.put("{jd_id}/", auth=JWTAuth())
def update_jd(request, jd_id: int, jd: JDIn, file: File[UploadedFile]):
    try: 
        jd_obj = JD.objects.get(id=jd_id, trust=get_user_trust(request.user))
    except JD.DoesNotExist:
        raise HttpError(404, "JD not found")

    jd_obj = save_jd(request, jd, file, jd_obj)
    return {"id": jd_obj.id}

@router.get("/panel", auth=JWTAuth(), response=JDPanel)
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

@router.get("/ids", auth=JWTAuth(), response=JDIDsOut)
def get_jd_ids(request):
    all_jds = JD.objects.filter(trust=get_user_trust(request.user))
    return {"ids": [jd.id for jd in all_jds]}

@router.get("{jd_id}/", auth=JWTAuth(), response=JDOut)
def get_jd(request, jd_id: int):
    try:
        jd = JD.objects.get(id=jd_id, trust=get_user_trust(request.user))
    except JD.DoesNotExist:
        raise HttpError(404, "JD not found")

    return {
        'id': jd.id,
        'trust': jd.trust.name,
        'consultant_type': jd.consultant_type.get_name_display(),
        'primary_specialities': [ps.name for ps in jd.primary_specialities.all()],
        'sub_specialities': [ss.name for ss in jd.sub_specialities.all()]
    }

    try:
        jd = JD.objects.get(id=jd_id, trust=get_user_trust(request.user))
    except JD.DoesNotExist:
        raise HttpError(404, "JD not found")

    return {"checklist": jd.checklist} 



from ninja import Schema
from typing import List, Optional
from django.shortcuts import get_object_or_404
from .models import ChecklistAnswer, ChecklistQuestion

# Define Schemas
class QuestionOut(Schema):
    text: str
    required: bool

class AnswerOut(Schema):
    id: int
    present: bool
    page_numbers: Optional[str]
    description: Optional[str]

class ChecklistItemOut(Schema):
    question: QuestionOut
    answer: AnswerOut

class JDChecklistOut(Schema):
    jd_id: int
    checklist: List[ChecklistItemOut]

@router.get("{jd_id}/checklist/", auth=JWTAuth(), response=JDChecklistOut)
def get_jd_checklist(request, jd_id: int):
    jd = get_object_or_404(JD, id=jd_id)
    
    consultant_type = jd.consultant_type
    
    checklist_questions = ChecklistQuestion.objects.filter(consultant_type=consultant_type)
    
    answers = []
    for question in checklist_questions:
        answer, created = ChecklistAnswer.objects.get_or_create(
            jd=jd,
            checklist_question=question,
            defaults={'present': False, 'page_numbers': '', 'description': ''}
        )
        answers.append(answer)
    
    result = {
        "jd_id": jd.id,
        "checklist": [
            {
                "question":{
                    "text": a.checklist_question.question.text,
                    "required": a.checklist_question.required,
                },
                "answer":{
                    "id": a.id,
                    "present": a.present,
                    "page_numbers": a.page_numbers,
                    "description": a.description,
                }
            }
            for a in answers
        ]
    }
    return result
