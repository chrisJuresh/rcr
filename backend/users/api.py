from ninja import Router
from ninja.errors import HttpError
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from .schemas import UnauthenticatedUserIn, TokenIn, UserProfileIn, UserProfileOut
from .services import (
    create_unauthenticated_user,
    register_user,
    get_user_profile, 
    update_user_profile,
    user_exists,
    get_tokens_for_user
)
from trusts.services import get_user_trust, get_user_trusts
from roles.services import get_user_roles
from .models import UnauthenticatedUser
from .schemas import UserRolesOut, ReviewersOut
from trusts.schemas import TrustOut

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
    profile = get_user_profile(request.user)
    return profile

@router.put("/profile/", auth=JWTAuth(), response=UserProfileOut)
def update_profile(request, payload: UserProfileIn):
    update_user_profile(request.auth, payload)
    profile = get_user_profile(request.user)
    return profile

@router.get("/roles/", auth=JWTAuth(), response=UserRolesOut)
def get_roles(request):
    return {
        "roles": get_user_roles(request.auth, ['approved', 'requested']),
        "requested_roles": get_user_roles(request.auth, ['requested'])
    }

@router.get("/trust", auth=JWTAuth(), response=TrustOut)
def get_trust(request):
    try:
        return {
            "id": get_user_trust(request.auth).id,
            "name": get_user_trust(request.auth).name,
            "region": {"name": get_user_trust(request.auth).region.name}
        }
    except:
        raise HttpError(400, "Your selected Trust does not match any Approved Trusts.")