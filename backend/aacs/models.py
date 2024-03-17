from django.db import models

from jds.models import JD

class AAC(models.Model):
    jd = models.ManyToManyField(JD)
    submission_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
