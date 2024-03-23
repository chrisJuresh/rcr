from ninja import Router
from django.http import JsonResponse
from .schemas import UnauthenticatedUserIn, TokenIn, UserProfileOut, UserProfileIn
from .services import (
    create_unauthenticated_user,
    register_user,
    get_user_profile, 
    update_user_profile,
    user_exists,
    get_tokens_for_user
)
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from .models import UnauthenticatedUser
from ninja.errors import HttpError

router = Router()

@router.post("/register-unauthenticated")
def register_unauthenticated(request, user: UnauthenticatedUserIn):
    if user_exists(user.email):
        raise HttpError(400, "An authenticated user with that email already exists")
    
    create_unauthenticated_user(user)

@router.post("/register-authenticate")
def register_authenticate(request, token: TokenIn):
    unauth_user = get_object_or_404(UnauthenticatedUser, token=token.token)
    if user_exists(unauth_user.email):
        raise HttpError(400, "An authenticated user with that email already exists")
    
    user = register_user(unauth_user, token.token)
    tokens = get_tokens_for_user(user)
    return tokens

@router.get("/profile/", auth=JWTAuth(), response=UserProfileOut)
def get_profile(request):
    profile = get_user_profile(request.auth)
    return profile

@router.put("/profile/", auth=JWTAuth(), response=UserProfileOut)
def update_profile(request, payload: UserProfileIn):
    update_user_profile(request.auth, payload)
    profile = get_user_profile(request.auth)
    return profile