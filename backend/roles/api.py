from typing import List
from ninja import Router, Schema
from .models import Role

router = Router()

class RoleOut(Schema):
    id: int
    name: str

class RolesOut(Schema):
    roles: List[RoleOut]

@router.get("/roles/", response=RolesOut)
def get_roles(request):
    roles = [
        {'id': role.id, 'name': role.get_name_display()}
        for role in Role.objects.all()
    ]
    return {'roles': roles}
