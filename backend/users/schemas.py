from ninja import Schema, Field
from typing import List, Optional

class UserIn(Schema):
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')
    password: str = Field(..., min_length=8)

class TokenIn(Schema):
    token: str

class UnauthenticatedUserIn(Schema):
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')
    password: str = Field(..., min_length=8)
    token: str

class UserRoleOut(Schema):
    name: str

class UserTrustOut(Schema):
    name: str

class UserProfileIn(Schema):
    title: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    trust: Optional[int] = None
    roles: Optional[List[int]] = None

class UserProfileOut(Schema):
    email: str
    title: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    trust: Optional[str]
    approved_trusts: Optional[List[UserTrustOut]]
    roles: Optional[List[UserRoleOut]]
    approved_roles: Optional[List[UserRoleOut]]

