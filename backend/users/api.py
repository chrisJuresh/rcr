from ninja import Router
from django.shortcuts import get_object_or_404
from ninja_jwt.authentication import JWTAuth
from .schemas import UserIn, UserProfileOut, UserProfileIn, UnauthenticatedUserIn, TokenIn
from .services import create_user, get_token_for_user, update_user_profile, get_user_roles, get_approved_roles, create_unauthenticated_user, user_exists
from typing import List
from .models import UnauthenticatedUser
from django.db import transaction
from django.http import HttpResponse

router = Router()

@router.post("/register-unauthenticated", url_name="register-unauthenticated")
def register_unauthenticated(request, user_in: UnauthenticatedUserIn):
    if user_exists(user_in.email):
        return HttpResponse("An authenticated user with that email already exists", status=400)
    else:
        create_unauthenticated_user(user_in.email, user_in.password, user_in.token)

@router.post("/register-validate", url_name="register-validate")
def register(request, user_in: TokenIn):
    unauth_user = get_object_or_404(UnauthenticatedUser, token=user_in.token)
    if user_exists(unauth_user.email):
        return HttpResponse("An authenticated user with that email already exists", status=400)
        
    with transaction.atomic():
        user = create_user(unauth_user.email, unauth_user.password)
        
        #unauth_user.delete()

        tokens = get_token_for_user(user)

        return {
            'message': 'User registered successfully',
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        }

@router.get("/profile/", auth=JWTAuth(), response=UserProfileOut)
def get_profile(request):
    user = request.auth
    user_roles = get_user_roles(user)
    approved_roles = get_approved_roles(user)
    user_trust = user.trust.name if user.trust else None
    return {**user.__dict__, 'trust': user_trust, 'roles': user_roles, 'approved_roles': approved_roles}

@router.put("/profile/", auth=JWTAuth())
def update_profile(request, payload: UserProfileIn):
    user = request.auth
    updated_user = update_user_profile(user, payload)
    return


    