from ninja import Schema, Field
from typing import List, Optional

class UserIn(Schema):
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')
    password: str = Field(..., min_length=8)

class UserRolesIn(Schema):
    id: int

class UserRolesOut(Schema):
    name: str

class UserApprovedRolesOut(Schema):
    name: str

class UserProfileIn(Schema):
    title: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[UserRolesIn]]

class UserProfileOut(Schema):
    email: str
    title: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    trust: Optional[str]
    roles: Optional[List[UserRolesOut]]
    approved_roles: Optional[List[UserApprovedRolesOut]]
