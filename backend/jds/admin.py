from django.contrib import admin
from .models import JD, JDProcess, Question, ChecklistQuestion, ChecklistAnswer

admin.site.register(JD)
admin.site.register(JDProcess)
admin.site.register(Question)
admin.site.register(ChecklistQuestion)
admin.site.register(ChecklistAnswer)
