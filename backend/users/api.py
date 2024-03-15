from ninja import Router
from django.shortcuts import get_object_or_404
from ninja_jwt.authentication import JWTAuth
from .schemas import UserIn, UserProfileOut, UserProfileIn, UnauthenticatedUserIn, TokenIn
from .services import create_user, get_token_for_user, update_user_profile, get_user_roles, get_approved_roles, create_unauthenticated_user, user_exists
from typing import List
from .models import UnauthenticatedUser
from django.db import transaction
from django.contrib.auth.hashers import make_password
from .models import UnauthenticatedUser, User

router = Router()

@router.post("/register-unauthenticated", url_name="register-unauthenticated")
def register_unauthenticated(request, user_in: UnauthenticatedUserIn):
    if user_exists(user_in.email):
        return {"message": "A user with that email already exists"}
    else:
        create_unauthenticated_user(user_in.email, user_in.password, user_in.token)
        return {"message": "User created successfully"}


@router.post("/register-validate", url_name="register-validate")
def register(request, user_in: TokenIn):
    unauth_user = get_object_or_404(UnauthenticatedUser, token=user_in.token)
    
    if user_exists(unauth_user.email):
        return {"message": "A user with this email already exists"}
        
    with transaction.atomic():
        # Create a new user instance without saving it to the database yet
        user = User(email=unauth_user.email)
        # Hash the unauthenticated user's password before setting it
        user.set_password(unauth_user.password)
        user.save()  # Now save the user after setting the hashed password

        # Delete the unauthenticated user record
        unauth_user.delete()

        # Generate JWT tokens for the new user
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


    