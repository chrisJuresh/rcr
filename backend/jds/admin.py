from django.contrib import admin
from .models import JD, Question, ChecklistQuestion, ChecklistAnswer

admin.site.register(JD)
admin.site.register(Question)
admin.site.register(ChecklistQuestion)
admin.site.register(ChecklistAnswer)
