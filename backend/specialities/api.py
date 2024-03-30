from typing import List
from ninja import Router, Schema
from .models import Speciality

router = Router()

class ConsultantTypeOut(Schema):
    name: str

class SpecialityOut(Schema):
    id: int
    name: str
    consultant_type: ConsultantTypeOut

class SpecialitiesOut(Schema):
    specialities: List[SpecialityOut]

@router.get("/specialities/", response=SpecialitiesOut)
def get_specialities(request):
    specialities = [
        {
            'id': speciality.id, 
            'name': speciality.name, 
            'consultant_type': {'name': speciality.consultant_type.name}
        } 
        for speciality in Speciality.objects.all()
    ]

    return {'specialities': specialities}

