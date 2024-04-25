from django.db import models

from jds.models import JD
from trusts.models import Trust
from specialities.models import ConsultantType
from users.models import User

class AAC(models.Model):
    jds = models.ManyToManyField(JD)

    trust = models.ForeignKey(Trust, on_delete=models.CASCADE)
    
    consultant_type = models.ForeignKey(ConsultantType, on_delete=models.CASCADE)

    submission_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField()

    representative = models.ForeignKey(User, on_delete=models.CASCADE)