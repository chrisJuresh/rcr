from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)


from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from ninja import Schema, Field
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from ninja.errors import ValidationError

User = get_user_model()

class UserCreateSchema(Schema):
    username: str = Field(..., pattern=r'^\S+@\S+\.\S+$')  
    password: str = Field(..., min_length=8)

from ninja_jwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api.post("/register", url_name="register")
def register(request, user_in: UserCreateSchema):
    if User.objects.filter(username=user_in.username).exists():
        raise ValidationError({'username': 'A user with that username already exists.'})

    user = User.objects.create(
        username=user_in.username,
        password=make_password(user_in.password)  
    )

    tokens=get_tokens_for_user(user)

    return {"tokens": tokens}

#login at /api/token/pair