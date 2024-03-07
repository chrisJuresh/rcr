from ninja import Router
from django.shortcuts import get_object_or_404
from ninja_jwt.authentication import JWTAuth
from .schemas import UserIn, UserProfileOut, UserProfileIn, RoleOut
from .services import create_user, get_token_for_user, update_user_profile, get_user_roles, get_all_roles
from typing import List

router = Router()

@router.post("/register", url_name="register")
def register(request, user_in: UserIn):
    user = create_user(user_in.email, user_in.password)
    tokens = get_token_for_user(user)
    return {"tokens": tokens}

@router.get("/roles/", response=List[RoleOut])
def get_roles(request):
    return get_all_roles()

@router.get("/profile/", auth=JWTAuth(), response=UserProfileOut)
def get_profile(request):
    user = request.auth
    user_roles = get_user_roles(user)
    return {**user.__dict__, 'roles': user_roles}

@router.put("/profile/", auth=JWTAuth(), response=UserProfileIn)
def update_profile(request, payload: UserProfileIn):
    updated_user = update_user_profile(request.auth, payload.dict())
    return updated_user 
