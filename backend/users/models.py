from django.contrib.auth.models import AbstractUser
from django.db import models
from trusts.models import Trust

class User(AbstractUser):
    trust = models.ForeignKey(Trust, on_delete=models.CASCADE, null=True, blank=True)