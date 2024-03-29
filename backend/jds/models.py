from django.db import models
from trusts.models import Trust
from specialities.models import ConsultantType, Speciality
from users.models import User
from simple_history.models import HistoricalRecords 

from viewflow.workflow.models import Process

class JD(models.Model):
    file = models.FileField(upload_to='JDs/')
    trust = models.ForeignKey(Trust, on_delete=models.CASCADE)

    consultant_type = models.ForeignKey(ConsultantType, on_delete=models.CASCADE)

    primary_specialities = models.ManyToManyField(Speciality, related_name='primary_specialities')
    sub_specialities = models.ManyToManyField(Speciality, related_name='sub_specialities', blank=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    history = HistoricalRecords() 

    def __str__(self):
        return str(self.id)

class JDProcess(Process):
    jd = models.ForeignKey(JD, on_delete=models.CASCADE)

    submission_date = models.DateTimeField(auto_now_add=True)

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    rcr_approved = models.BooleanField(default=False)
    rsa_approved = models.BooleanField(default=False)
    ammended = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    history = HistoricalRecords() 
