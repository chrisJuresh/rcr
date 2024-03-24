from typing import List
from ninja import Router, Schema
from .models import Trust

router = Router()

class RegionOut(Schema):
    name: str

class TrustOut(Schema):
    id: int
    name: str
    region: RegionOut

class TrustsOut(Schema):
    trusts: List[TrustOut]

@router.get("/trusts/", response=TrustsOut)
def get_trusts(request):
    trusts = [
        {
            'id': trust.id, 
            'name': trust.name, 
            'region': {'name': trust.region.name}
        } 
        for trust in Trust.objects.all()
    ]

    return {'trusts': trusts}

