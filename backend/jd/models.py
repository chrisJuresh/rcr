from django.db import models
from trusts.models import Trust
from speciality.models import Speciality, ConsultantType

class JD(models.Model):
    document = models.FileField(upload_to='jd_documents/')
    submission_date = models.DateTimeField(auto_now_add=True)

    trust = models.ForeignKey(Trust, on_delete=models.CASCADE, null=True)

    consultantType = models.ForeignKey(ConsultantType, on_delete=models.CASCADE)

    primarySpecialities = models.ManyToManyField(Speciality, related_name='primary_speciality')
    subSpecialities = models.ManyToManyField(Speciality, related_name='sub_speciality')
