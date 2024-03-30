from django.contrib import admin
from .models import User, UserProfile, UserRole, UnauthenticatedUser

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserRole)
admin.site.register(UnauthenticatedUser)