from django.contrib import admin
from .models import User, UserTrust, UserRole, UserSpecialities, UnauthenticatedUser

admin.site.register(User)
admin.site.register(UserTrust)
admin.site.register(UserRole)
admin.site.register(UserSpecialities)
admin.site.register(UnauthenticatedUser)