from ninja import Router, File
from ninja.errors import HttpError
from ninja.files import UploadedFile
from ninja_jwt.authentication import JWTAuth
from django.utils.dateformat import format
from typing import Optional
from .schemas import JDIn, JDPanel, JDOut, JDIDsOut, JDID, JDChecklistOut, JDChecklistIn
from .models import JD, ChecklistAnswer, ChecklistQuestion
from trusts.services import get_user_trust, get_user_trusts
from roles.services import get_user_roles
from .services import save_jd, user_jds
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404
from transitions.extensions import GraphMachine
from .models import JDStateMachine
from users.services import get_valid_users
from users.schemas import ReviewersOut

router = Router()

@router.post("/jd/", auth=JWTAuth(), response=JDID)
def create_jd(request, jd: JDIn, file: File[UploadedFile]):
    jd_obj = save_jd(request, jd, file)
    jd_obj.create()
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
def get_jd_panel(request, panel: Optional[str] = None):
    all_jds = user_jds(request.user, panel)
    
    jds = [{
        'id': jd.id,
        'status': jd.status,
        'date': jd.status_date.strftime('%y-%m-%d %H:%M') if jd.status_date else None,
        'consultant_type': jd.consultant_type.get_name_display(),
        'primary_specialties': [ps.name for ps in jd.primary_specialities.all()],
        'sub_specialties': [ss.name for ss in jd.sub_specialities.all()],
    } for jd in all_jds]

    return {'jds': jds}

@router.get("/ids", auth=JWTAuth(), response=JDIDsOut)
def get_jd_ids(request):
    jds = user_jds(request.user)
    return {"ids": [jd.id for jd in jds]}

@router.get("{jd_id}/", auth=JWTAuth(), response=JDOut)
def get_jd(request, jd_id: int):
    try:
        jds = user_jds(request.user)
        jd = jds.get(id=jd_id)
    except JD.DoesNotExist:
        raise HttpError(404, "JD not found")

    return {
        'id': jd.id,
        'file': jd.file,
        'status': jd.status,
        'reviewer': jd.reviewer.get_full_name() if jd.reviewer else None,
        'date': jd.status_date.strftime('%y-%m-%d %H:%M') if jd.status_date else None,
        'trust': jd.trust.name,
        'consultant_type': jd.consultant_type.get_name_display(),
        'primary_specialities': [ps.name for ps in jd.primary_specialities.all()],
        'sub_specialities': [ss.name for ss in jd.sub_specialities.all()],
        'state_diagram': jd.diagram if jd.diagram else '',
    }

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
        "requirements_met": jd.requirements_met,
        "checklist": [
            {
                "question":{
                    "id": a.checklist_question.id,
                    "text": a.checklist_question.question.text,
                    "required": a.checklist_question.required,
                },
                "answer":{
                    "id": a.id,
                    "present": a.present,
                    "page_numbers": a.page_numbers,
                    "description": a.description,
                    "rcr_comments": a.rcr_comments,
                    "rsa_comments": a.rsa_comments,
                }
            }
            for a in answers
        ]
    }
    return result

@router.put("{jd_id}/checklist/", auth=JWTAuth(), response=JDChecklistOut)
def update_jd_checklist(request, jd_id: int, jd_checklist: JDChecklistIn, panel: Optional[str] = None):
    jd = get_object_or_404(JD, id=jd_id)

    if (panel == "Edit") and (jd.trust == get_user_trust(request.user)) and ('Trust Employee' in get_user_roles(request.user, 'approved')):
            with transaction.atomic():
                all_required_met = True 
          
                for item in jd_checklist.checklist:
                    question = get_object_or_404(ChecklistQuestion, id=item.question.id)
          
                    answer, created = ChecklistAnswer.objects.get_or_create(
                        jd=jd,
                        checklist_question=question,
                        defaults={
                            'present': item.answer.present,
                            'page_numbers': item.answer.page_numbers or '',
                            'description': item.answer.description or ''
                        }
                    )
                    
                    if not created:
                        answer.present = item.answer.present
                        answer.page_numbers = item.answer.page_numbers
                        answer.description = item.answer.description
                        answer.save()
          
                    if question.required and (not answer.present or not answer.page_numbers):
                        all_required_met = False
          
                jd.requirements_met = all_required_met
                jd.save() 
    
    elif ((panel=="Review") and ('RCR Employee' in get_user_roles(request.user, 'approved'))):
        with transaction.atomic():
            for item in jd_checklist.checklist:
                answer = get_object_or_404(ChecklistAnswer, id=item.answer.id)
                
                answer.rcr_comments = item.answer.rcr_comments or ''
                answer.save()

    answers = ChecklistAnswer.objects.filter(jd=jd)
    
    result = {
        "jd_id": jd.id,
        "requirements_met": jd.requirements_met,
        "checklist": [
            {
                "question": {
                    "id": a.checklist_question.id,
                    "text": a.checklist_question.question.text,
                    "required": a.checklist_question.required,
                },
                "answer": {
                    "id": a.id,
                    "present": a.present,
                    "page_numbers": a.page_numbers,
                    "description": a.description,
                    "rcr_comments": a.rcr_comments,
                    "rsa_comments": a.rsa_comments,
                }
            } for a in answers
        ]
    }
    return result

from users.models import User

@router.put("{jd_id}/{state}/", auth=JWTAuth()) 
def update_jd_state(request, jd_id: int, state: str, reviewer: Optional[str]=None):
    if state == 'submit' and 'Trust Employee' in get_user_roles(request.user, 'approved'):
        jd = JD.objects.get(id=jd_id, trust=get_user_trust(request.user))
        jd.submit()
    elif state == 'approve' and ('RCR Employee' or 'Reviewer' in get_user_roles(request.user, 'approved')):
        jd = JD.objects.get(id=jd_id)
        if 'RCR Employee' in get_user_roles(request.user, ['approved', 'requested']):
            jd.reviewer = User.objects.get(id=reviewer)
        jd.approve()
    elif state == 'reject' and 'RCR Employee' or 'Reviewer' in get_user_roles(request.user, 'approved'):
        jd = JD.objects.get(id=jd_id)
        jd.reject()
