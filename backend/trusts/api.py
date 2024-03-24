from typing import List
from ninja import Router, Schema
from .models import Trust

router = Router()

class RegionOut(Schema):
    name: str

class TrustOut(Schema):
    id: int
    name: str

class TrustInfoOut(Schema):
    id: int
    name: str
    region: RegionOut

@router.get("/trusts/", response=List[TrustInfoOut])
def get_trusts(request):
    return [
        {
            'id': trust.id, 
            'name': trust.name, 
            'region': {'name': trust.region.name}
        } 
        for trust in Trust.objects.all()
    ]

