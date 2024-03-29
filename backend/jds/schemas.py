from ninja import Schema
from typing import List, Optional


class JDIn(Schema):
    consultant_type: str
    primary_specialities: List[int]
    sub_specialities: Optional[List[int]]

class PanelJD(Schema):
    id: int
    consultant_type: str
    primary_specialties: List[str]
    sub_specialties: Optional[List[str]]
    date: str

class JDPanel(Schema):
    jds: List[PanelJD]