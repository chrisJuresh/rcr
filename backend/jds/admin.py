from django.contrib import admin
from .models import JD, Question, ChecklistQuestion, ChecklistAnswer

class JDAdmin(admin.ModelAdmin):
    readonly_fields = ('status_date',)

admin.site.register(JD,JDAdmin)
admin.site.register(Question)
admin.site.register(ChecklistQuestion)
admin.site.register(ChecklistAnswer)
