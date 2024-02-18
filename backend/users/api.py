from typing import Any
from django.contrib.auth import get_user_model, logout, authenticate
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from ninja import NinjaAPI, Schema
from ninja.security import django_auth
from .models import Role, Trust
from .schemas import LoginSchema, RegisterSchema, UserSchema, RoleSchema, TokenSchema # You need to create these schema classes based on your DRF serializers

User = get_user_model()
api = NinjaAPI()

class MessageSchema(Schema):
    message: str

# Login API
@api.post("login", response={200: TokenSchema, 400: MessageSchema})
def login(request, payload: LoginSchema):
    user = authenticate(username=payload.username, password=payload.password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return 200, {"token": token.key}
    return 400, {"message": "Invalid Credentials"}

# Register API
@api.post("register", response={201: TokenSchema, 400: MessageSchema})
def register(request, payload: RegisterSchema):
    try:
        user = User.objects.create_user(
            username=payload.username,
            password=payload.password,
        )
        token, _ = Token.objects.get_or_create(user=user)
        return 201, {"token": token.key}
    except IntegrityError:
        return 400, {"message": "A user with that username already exists"}

# Profile API
@api.get("profile", auth=django_auth, response={200: UserSchema, 400: MessageSchema})
def get_profile(request):
    return 200, UserSchema.from_orm(request.auth)

@api.put("profile", auth=django_auth, response={200: UserSchema, 400: MessageSchema})
def update_profile(request, payload: UserSchema):
    user = request.auth
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    user.save()
    return 200, UserSchema.from_orm(user)

# Validate Token API
@api.get("validate-token", auth=django_auth, response={200: UserSchema})
def validate_token(request):
    return 200, UserSchema.from_orm(request.auth)

# Role API
@api.get("roles", response={200: list[RoleSchema]})
def list_roles(request):
    roles = Role.objects.all()
    return 200, [RoleSchema.from_orm(role) for role in roles]

# Logout API
@api.get("logout")
def logout_view(request):
    logout(request)
    return {"message": "Logged out successfully"}


