from ninja import Schema, Field
from typing import List, Optional
from trusts.schemas import TrustOut, TrustsOut

class UserIn(Schema):
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')
    password: str = Field(..., min_length=8)

class TokenIn(Schema):
    token: str

class UnauthenticatedUserIn(Schema):
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')
    password: str = Field(..., min_length=8)
    token: str

class SpecialitiesOut(Schema):
    id: int
    name: str

class UserRolesOut(Schema):
    roles: List[str]
    requested_roles: List[str]

class UserProfileIn(Schema):
    title: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    trust: Optional[int] = None
    roles: Optional[List[int]] = None
    consultant_type: Optional[str] = None
    specialities: Optional[List[int]] = None

class UserProfileOut(Schema):
    email: str
    title: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    trust: Optional[TrustOut]
    approved_trusts: Optional[List[str]]
    roles: Optional[List[str]]
    approved_roles: Optional[List[str]]
    consultant_type: Optional[str]
    specialities: Optional[List[SpecialitiesOut]]
    updated: Optional[str]

class ReviewerOut(Schema):
    id: int
    name: str
    same_region: str
    trusts: List[TrustOut]

class ReviewersOut(Schema):
    reviewers: Optional[List[ReviewerOut]] = None

class RepOut(Schema):
    id: int
    consultant_type: str
    primary_specialties: List[str]
    status: str
    date: str   
    selected: bool

class RepsOut(Schema):
    reps: Optional[List[RepOut]] = None