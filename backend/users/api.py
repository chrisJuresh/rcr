from ninja import Router
from ninja.errors import HttpError
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from .schemas import UnauthenticatedUserIn, TokenIn, UserProfileIn, UserProfileOut
from .services import (
    create_unauthenticated_user,
    register_user,
    get_user_profile, 
    update_user_profile,
    user_exists,
    get_tokens_for_user,
    get_valid_users
)
from trusts.services import get_user_trust, get_user_trusts
from roles.services import get_user_roles
from .models import UnauthenticatedUser
from .schemas import UserRolesOut, ReviewersOut, RepsOut, TokenOut
from trusts.schemas import TrustOut
from jds.models import JD
from aacs.models import AAC

router = Router()

@router.post("/register-unauthenticated")
def register_unauthenticated(request, user: UnauthenticatedUserIn):
    if user_exists(user.email):
        raise HttpError(400, "An authenticated user with that email already exists")
    
    create_unauthenticated_user(user)

@router.post("/register-authenticate", response=TokenOut)
def register_authenticate(request, token: TokenIn):
    unauth_user = get_object_or_404(UnauthenticatedUser, token=token.token)
    if user_exists(unauth_user.email):
        raise HttpError(400, "An authenticated user with that email already exists")
    
    user = register_user(unauth_user, token.token)
    tokens = get_tokens_for_user(user)
    return tokens

@router.get("/profile/", auth=JWTAuth(), response=UserProfileOut)
def get_profile(request):
    profile = get_user_profile(request.user)
    return profile

@router.put("/profile/", auth=JWTAuth(), response=UserProfileOut)
def update_profile(request, payload: UserProfileIn):
    update_user_profile(request.auth, payload)
    profile = get_user_profile(request.user)
    return profile

@router.get("/roles/", auth=JWTAuth(), response=UserRolesOut)
def get_roles(request):
    return {
        "roles": get_user_roles(request.auth, ['approved', 'requested']),
        "requested_roles": get_user_roles(request.auth, ['requested'])
    }

@router.get("/trust", auth=JWTAuth(), response=TrustOut)
def get_trust(request):
    try:
        return {
            "id": get_user_trust(request.auth).id,
            "name": get_user_trust(request.auth).name,
            "region": {"name": get_user_trust(request.auth).region.name}
        }
    except:
        raise HttpError(400, "Your selected Trust does not match any Approved Trusts.")

@router.get("/reps/{aac_id}/", auth=JWTAuth(), response=RepsOut)
def get_reps(request, aac_id: int):
    aac = AAC.objects.get(id=aac_id)
    all_reps = get_valid_users(task=aac, role="Representative")
    reps = [
    {
        'id': rep.id,
        'consultant_type': rep.user_specialities.consultant_type.get_name_display(),
        'primary_specialties': [ps.name for ps in rep.user_specialities.specialities.all()],
        'status': rep.email,
        'date': rep.date_joined.strftime("%A"),
        'selected': aac.representative == rep
    } for rep in all_reps
    ]
    return {"reps": reps}


@router.get("/reviewers/{jd_id}", auth=JWTAuth(), response=ReviewersOut)
def get_reviewers(request, jd_id: int):
    if 'RCR Employee' in get_user_roles(request.user, 'approved'):
        jd = JD.objects.get(id=jd_id)
        all_reviewers = get_valid_users(task=jd, role='Reviewer')
        reviewers = [
            {
                'id': reviewer.id,
                'name': reviewer.get_full_name(),
                'same_region': "Same Region" if reviewer.user_trusts.filter(trust__region=jd.trust.region, approved=True).exists() else "Other Regions",
                'trusts': [
                    {
                        'id': trust.id, 
                        'name': trust.name, 
                        'region': {'name': trust.region.name}
                    } for trust in get_user_trusts(reviewer, 'approved')
                ]
            } for reviewer in all_reviewers
        ]
        return {
            "reviewers": reviewers
        }
    
    else:
        return {"reviewers": []}