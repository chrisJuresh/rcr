from ninja import Schema, ModelSchema
from typing import List, Optional
from django.contrib.auth import get_user_model
from .models import Role, Trust  # Assuming these are your models

User = get_user_model()

class TokenSchema(Schema):
    token: str

class LoginSchema(Schema):
    username: str
    password: str

class RegisterSchema(Schema):
    username: str
    password: str

class TrustSchema(ModelSchema):
    class Config:
        model = Trust
        model_fields = ['id', 'name']

class RoleSchema(ModelSchema):
    class Config:
        model = Role
        model_fields = ['id', 'name']

class UserSchema(ModelSchema):
    trust: Optional[TrustSchema] = None
    roles: List[RoleSchema] = []
    can_be_reviewer: Optional[bool] = None
    can_be_representative: Optional[bool] = None
    can_be_rcr_employee: Optional[bool] = None

    class Config:
        model = User
        model_fields = ['username', 'first_name', 'last_name']