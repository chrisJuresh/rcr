from ninja import Router, File
from ninja.errors import HttpError
from ninja.files import UploadedFile
from ninja_jwt.authentication import JWTAuth
from django.utils.dateformat import format
from typing import Optional
from .schemas import JDIn, JDPanel, JDOut, JDIDsOut, JDID
from .models import JD
from trusts.services import get_user_trust
from .services import save_jd, user_jds

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
    #all_jds = JD.objects.filter(trust=get_user_trust(request.user))
    
    #if status:
    #    all_jds = all_jds.filter(status=status)

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
        'status': jd.status,
        'date': jd.status_date.strftime('%y-%m-%d %H:%M') if jd.status_date else None,
        'trust': jd.trust.name,
        'consultant_type': jd.consultant_type.get_name_display(),
        'primary_specialities': [ps.name for ps in jd.primary_specialities.all()],
        'sub_specialities': [ss.name for ss in jd.sub_specialities.all()],
        'state_diagram': jd.diagram if jd.diagram else '',
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
    id: int
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
    requirements_met: bool
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
                }
            }
            for a in answers
        ]
    }
    return result


from django.db import transaction

class QuestionIn(Schema):
    id: int
    text: str
    required: bool

class AnswerIn(Schema):
    id: int
    present: bool
    page_numbers: Optional[str]
    description: Optional[str]

class ChecklistItemIn(Schema):
    question: QuestionIn
    answer: AnswerIn

class JDChecklistIn(Schema):
    jd_id: int
    requirements_met: bool
    checklist: List[ChecklistItemIn]

@router.put("{jd_id}/checklist/", auth=JWTAuth(), response=JDChecklistOut)
def update_jd_checklist(request, jd_id: int, jd_checklist: JDChecklistIn):
    jd = get_object_or_404(JD, id=jd_id)

    with transaction.atomic():
        all_required_met = True  # Assume all required answers are met initially

        for item in jd_checklist.checklist:
            question = get_object_or_404(ChecklistQuestion, id=item.question.id)

            # Find or create the answer linked to the JD and the question
            answer, created = ChecklistAnswer.objects.get_or_create(
                jd=jd,
                checklist_question=question,
                defaults={
                    'present': item.answer.present,
                    'page_numbers': item.answer.page_numbers or '',
                    'description': item.answer.description or ''
                }
            )
            
            # If not created, update the answer with provided data
            if not created:
                answer.present = item.answer.present
                answer.page_numbers = item.answer.page_numbers
                answer.description = item.answer.description
                answer.save()

            # Check if the question is required and the answer is not adequately filled
            # Now it checks both 'present' and 'page_numbers'
            if question.required and (not answer.present or not answer.page_numbers):
                all_required_met = False

        # Update the JD requirements_met attribute based on the answers' completeness
        jd.requirements_met = all_required_met
        jd.save()  # Save the JD status update
    
    # After updating, fetch updated answers to return them
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
                }
            } for a in answers
        ]
    }
    return result

from django.shortcuts import get_object_or_404
from transitions.extensions import GraphMachine
from .models import JDStateMachine

@router.put("{jd_id}/submit/", auth=JWTAuth()) 
def submit_jd(request, jd_id: int):
    jd = JD.objects.get(id=jd_id, trust=get_user_trust(request.user))

    jd.submit()
    