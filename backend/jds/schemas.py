from ninja import Schema
from typing import List, Optional

class JDID(Schema):
    id: int

class JDIn(Schema):
    consultant_type: str
    primary_specialities: List[int]
    sub_specialities: Optional[List[int]]

class JDIDsOut(Schema):
    ids: List[int]

class JDOut(Schema):
    id: int
    file: str
    trust: str
    status: str
    reviewer: Optional[str]
    date: str
    consultant_type: str
    primary_specialities: List[str]
    sub_specialities: Optional[List[str]]
    state_diagram: Optional[str]

class PanelJD(Schema):
    id: int
    status: str
    date: str
    consultant_type: str
    primary_specialties: List[str]
    sub_specialties: Optional[List[str]]

class JDPanel(Schema):
    jds: List[PanelJD]

# Checklist Out 
class QuestionOut(Schema):
    id: int
    text: str
    required: bool

class AnswerOut(Schema):
    id: int
    present: bool
    page_numbers: Optional[str]
    description: Optional[str]
    rcr_comments: Optional[str]
    rsa_comments: Optional[str]

class ChecklistItemOut(Schema):
    question: QuestionOut
    answer: AnswerOut

class JDChecklistOut(Schema):
    jd_id: int
    requirements_met: bool
    checklist: List[ChecklistItemOut]

# Checklist In
class QuestionIn(Schema):
    id: int
    text: str
    required: bool

class AnswerIn(Schema):
    id: int
    present: bool
    page_numbers: Optional[str]
    description: Optional[str]
    rcr_comments: Optional[str] = None
    rsa_comments: Optional[str] = None

class ChecklistItemIn(Schema):
    question: QuestionIn
    answer: AnswerIn

class JDChecklistIn(Schema):
    jd_id: int
    requirements_met: bool
    checklist: List[ChecklistItemIn]