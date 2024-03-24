from django.db import models
from trusts.models import Trust
from specialities.models import ConsultantType, Speciality
from users.models import User
from simple_history.models import HistoricalRecords 

class JD(models.Model):
    file = models.FileField(upload_to='JDs/')
    trust = models.ForeignKey(Trust, on_delete=models.CASCADE)

    consultant_type = models.ForeignKey(ConsultantType, on_delete=models.CASCADE)

    primary_specialities = models.ManyToManyField(Speciality, related_name='primary_specialities')
    sub_specialities = models.ManyToManyField(Speciality, related_name='sub_specialities', blank=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    submission_date = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()  