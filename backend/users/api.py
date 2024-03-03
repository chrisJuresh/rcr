from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from ninja import Schema, Field
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from ninja.orm import create_schema
from .models import Role
from typing import List

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
User = get_user_model()

class UserIn(Schema):
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')  
    password: str = Field(..., min_length=8)

def get_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api.post("/register", url_name="register")
def register(request, user_in: UserIn):
    if User.objects.filter(email=user_in.email).exists():
        raise ValidationError('A user with that email already exists')

    user = User.objects.create(
        email=user_in.email,
        password=make_password(user_in.password)  
    )

    tokens=get_token(user)

    return {"tokens": tokens}

#login at /api/token/pair
#verify at /api/token/verify
 
class UserRolesOut(Schema):
    name: str

class UserProfileOut(Schema):
    email: str | None
    title: str | None
    first_name: str | None
    last_name: str | None
    roles: List[UserRolesOut] | None

@api.get("/profile/", auth=JWTAuth(), response=UserProfileOut)
def get_profile(request):
    user = request.auth
    user_profile = {
        'email': user.email,
        'title': user.title,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'roles': [{
            'name': role.get_name_display() 
        } for role in user.roles.all()]
    }
    return user_profile

class UserRolesIn(Schema):
    id: int
    name: str

class UserProfileIn(Schema):
    title: str | None  
    first_name: str | None
    last_name: str | None
    roles: List[UserRolesIn] | None

@api.put("/profile/", auth=JWTAuth(), response=UserProfileIn)
def update_profile(request, payload: UserProfileIn):
    user = request.auth
    for attr, value in payload.dict().items():
        if value is not None and value != "":
            setattr(user, attr, value)
    user.save()
    return user

class RoleOut(Schema):
    id: int
    name: str

@api.get("/roles/", response=List[RoleOut])
def get_roles(request):
    roles = Role.objects.all()
    readable_roles = [{'id': role.id, 'name': role.get_name_display()} for role in roles]
    return readable_roles