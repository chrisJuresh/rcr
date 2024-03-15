from django.contrib import admin
from .models import User, UserRole, ReviewerInfo, RepresentativeInfo, UnauthenticatedUser

admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(ReviewerInfo)
admin.site.register(UnauthenticatedUser)