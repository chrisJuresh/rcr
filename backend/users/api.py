from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from ninja import Schema, Field
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404

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
 
class UserProfileOut(Schema):
    email: str
    first_name: str
    last_name: str

@api.get("/profile/", auth=JWTAuth(), response=UserProfileOut)
def get_profile(request):
    user = request.auth
    return UserProfileOut(email=user.email, first_name=user.first_name, last_name=user.last_name)

class UserProfileIn(Schema):
    first_name: str
    last_name: str

@api.put("/profile/", auth=JWTAuth(), response=UserProfileIn)
def update_profile(request, payload: UserProfileIn):
    user = request.auth
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    return UserProfileIn(first_name=user.first_name, last_name=user.last_name)