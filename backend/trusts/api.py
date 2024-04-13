from .models import Trust
from .schemas import TrustsOut
from ninja import Router

router = Router()

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