from ninja import Schema, Field
from typing import List, Optional

class UserIn(Schema):
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')
    password: str = Field(..., min_length=8)

class UserRolesOut(Schema):
    name: str

class UserProfileOut(Schema):
    email: Optional[str]
    title: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[UserRolesOut]]

class UserRolesIn(Schema):
    id: int
    name: str

class UserProfileIn(Schema):
    title: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[UserRolesIn]]

class RoleOut(Schema):
    id: int
    name: str