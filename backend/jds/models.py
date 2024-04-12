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

class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question

class ChecklistQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    consultant_type = models.ForeignKey(ConsultantType, on_delete=models.CASCADE, related_name='checklists')
    
    required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.consultant_type.name}: {self.question.question}"
    

class ChecklistAnswer(models.Model):
    jd = models.ForeignKey(JD, on_delete=models.CASCADE, related_name='answers')
    checklist_question = models.ForeignKey(ChecklistQuestion, on_delete=models.CASCADE, related_name='answers')

    present = models.BooleanField(default=False)
    page_numbers = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Answer to {self.checklist_question.question} for JD {self.jd.id}"