from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    ROLES = (
        ('REVIEWER', 'Reviewer'),
        ('REPRESENTATIVE', 'Representative'),
        ('TRUST_EMPLOYEE', 'Trust Employee'),
        ('RCR_EMPLOYEE', 'RCR Employee'),
    )
    name = models.CharField(max_length=20, choices=ROLES, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
#   trust = models.ForeignKey('Trust', on_delete=models.CASCADE, null=True, blank=True)
    roles = models.ManyToManyField(Role, through='UserRole', blank=True)
    title = models.CharField(max_length=4, blank=True, null=True)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user}'s role as {self.role}"

class ReviewerInfo(models.Model):
    user_role = models.OneToOneField(UserRole, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'role__name': 'REVIEWER'})
#    consultant_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_role.user}'s reviewer info"

class RepresentativeInfo(models.Model):
    user_role = models.OneToOneField(UserRole, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'role__name': 'REPRESENTATIVE'})
#    specialities = models.TextField()

    def __str__(self):
        return f"{self.user_role.user}'s representative info"