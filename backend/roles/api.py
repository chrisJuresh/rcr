from typing import List
from ninja import Router, Schema
from .models import Role

router = Router()

class RoleOut(Schema):
    id: int
    name: str

@router.get("/roles/", response=List[RoleOut])
def get_roles(request):
    return [{'id': role.id, 'name': role.get_name_display()} for role in Role.objects.all()]
