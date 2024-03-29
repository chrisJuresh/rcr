from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import JD, JDProcess

admin.site.register(JD)
admin.site.register(JDProcess)