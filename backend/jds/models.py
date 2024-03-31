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

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    rcr_approved = models.BooleanField(default=False)
    rsa_approved = models.BooleanField(default=False)
    ammended = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

class JDChecklist(models.Model):
    jd = models.OneToOneField(JD, related_name='checklist', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.jd.id + ' Checklist')

class ChecklistItem(models.Model):
    checklist = models.ForeignKey(JDChecklist, related_name='items', on_delete=models.CASCADE)

    consultant_type = models.ManyToManyField(ConsultantType)
    question = models.TextField()
    required = models.BooleanField(default=False)
    present = models.BooleanField(default=False)
    page_numbers = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.question