from django.contrib import admin
from .models import User, UserRole, Reviewer, UnauthenticatedUser

admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(Reviewer)
admin.site.register(UnauthenticatedUser)