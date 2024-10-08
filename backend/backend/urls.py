"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.api import router as users_router
from roles.api import router as roles_router
from trusts.api import router as trusts_router
from specialities.api import router as specialities_router
from jds.api import router as jds_router
from aacs.api import router as aacs_router
from .api import api
from django.conf import settings
from django.conf.urls.static import static

api.add_router("/users/", users_router, tags=["users"]),
api.add_router("/roles/", roles_router, tags=["roles"]),
api.add_router("/trusts/", trusts_router, tags=["trusts"]),
api.add_router("/specialities/", specialities_router, tags=["specialities"]),
api.add_router("/jds/", jds_router, tags=["jds"]),
api.add_router("/aacs/", aacs_router, tags=["aacs"]),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
