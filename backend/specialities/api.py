from typing import List
from ninja import Router, Schema
from .models import Speciality

router = Router()

class SpecialityOut(Schema):
    id: int
    name: str
    consultant_type: str

class SpecialitiesOut(Schema):
    specialities: List[SpecialityOut]

@router.get("/specialities/", response=SpecialitiesOut)
def get_specialities(request):
    specialities = [
        {
            'id': speciality.id, 
            'name': speciality.name, 
            'consultant_type': speciality.consultant_type.name
        } 
        for speciality in Speciality.objects.all()
    ]

    return {'specialities': specialities}

