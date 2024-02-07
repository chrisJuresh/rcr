from django.db import models
from trusts.models import Trust
from speciality.models import ConsultantBase

class JD(models.Model):
    document = models.FileField(upload_to='jd_documents/')
    submission_date = models.DateTimeField(auto_now_add=True)

    trust = models.ForeignKey(Trust, on_delete=models.CASCADE, null=True)

    radiologist = models.ForeignKey('speciality.Radiologist', on_delete=models.CASCADE, null=True, blank=True)
    oncologist = models.ForeignKey('speciality.Oncologist', on_delete=models.CASCADE, null=True, blank=True)