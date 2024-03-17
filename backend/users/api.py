from ninja import Router
from django.http import JsonResponse
from .schemas import UnauthenticatedUserIn, TokenIn, UserProfileOut, UserProfileIn
from .services import (
    create_unauthenticated_user,
    register_user,
    get_user_profile, 
    update_user_profile,
    user_exists
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
def register_authenticate(request, user: TokenIn):
    unauth_user = get_object_or_404(UnauthenticatedUser, token=user.token)
    if user_exists(unauth_user.email):
        raise HttpError(400, "An authenticated user with that email already exists")
    
    tokens = register_user(unauth_user, user.token)
    return tokens

@router.get("/profile/", auth=JWTAuth(), response=UserProfileOut)
def get_profile(request):
    return get_user_profile(request.auth)

@router.put("/profile/", auth=JWTAuth(), response=UserProfileOut)
def update_profile(request, payload: UserProfileIn):
    update_user_profile(request.auth, payload)
    return get_user_profile(request.auth)