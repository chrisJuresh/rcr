from ninja import Router
from django.http import JsonResponse
from .schemas import UnauthenticatedUserIn, TokenIn, UserProfileOut, UserProfileIn, JDPanel
from .services import (
    create_unauthenticated_user,
    register_user,
    get_user_profile, 
    update_user_profile,
    user_exists,
    get_tokens_for_user
)
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from .models import UnauthenticatedUser
from ninja.errors import HttpError

from jds.models import JD

router = Router()

@router.post("/register-unauthenticated")
def register_unauthenticated(request, user: UnauthenticatedUserIn):
    if user_exists(user.email):
        raise HttpError(400, "An authenticated user with that email already exists")
    
    create_unauthenticated_user(user)

@router.post("/register-authenticate")
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

from django.utils.dateformat import DateFormat  # Import Django's date format utility

@router.get("/jds/", auth=JWTAuth(), response=JDPanel)
def get_jd_panel(request):
    jds = JD.objects.filter(trust=request.user.trust)
    jd_panel = []

    for jd in jds:
        primary_specialties = [ps.name for ps in jd.primary_specialities.all()]
        sub_specialties = [ss.name for ss in jd.sub_specialities.all()]

        latest_edit_date = jd.history.first().history_date if jd.history.exists() else jd.submission_date
        latest_edit_date_str = DateFormat(latest_edit_date).format('Y-m-d H:i:s')  
 
        jd_panel.append({
            'id': jd.id,
            'consultant_type': jd.consultant_type.get_name_display(),
            'primary_specialties': primary_specialties,
            'sub_specialties': sub_specialties,
            'date': latest_edit_date_str 
        })

    return {'jd_panel': jd_panel}