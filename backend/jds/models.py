from django.db import models
from trusts.models import Trust
from specialities.models import ConsultantType, Speciality
from users.models import User

# JD model definition
class JD(models.Model):
    # Assuming you want to upload to 'uploads/' folder
    file = models.FileField(upload_to='JDs/')
    submission_date = models.DateTimeField(auto_now_add=True)
    trust = models.ForeignKey(Trust, on_delete=models.CASCADE)

    consultant_type = models.ForeignKey(ConsultantType, on_delete=models.CASCADE)

    primary_specialities = models.ManyToManyField(Speciality, related_name='primary_specialities')
    sub_specialities = models.ManyToManyField(Speciality, related_name='sub_specialities')

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
