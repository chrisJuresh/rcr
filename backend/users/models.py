from django.contrib.auth.models import AbstractUser
from django.db import models
from trusts.models import Trust

class Role(models.Model):
    ROLES = (
        ('REVIEWER', 'Reviewer'),
        ('REPRESENTATIVE', 'Representative'),
        ('TRUST_EMPLOYEE', 'Trust Employee'),
        ('RCR_EMPLOYEE', 'RCR Employee'),
        ('', 'None')
    )

    name = models.CharField(max_length=20, choices=ROLES, default='', unique=True)

    def __str__(self):
        return self.name
    
class RolePermissions(models.Model):
    can_be_reviewer = models.BooleanField(default=False)
    can_be_representative = models.BooleanField(default=False)
    can_be_rcr_employee = models.BooleanField(default=False)
  
class User(AbstractUser):
    trust = models.ForeignKey(Trust, on_delete=models.CASCADE, null=True, blank=True)
    roles = models.ManyToManyField(Role, blank=True)
    perms = models.ForeignKey(RolePermissions, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        role = kwargs.pop('role', None)

        super().save(*args, **kwargs)

        if role:
            if role.name == 'REVIEWER' and self.perms.can_be_reviewer:
                self.roles.add(role)
            elif role.name == 'REPRESENTATIVE' and self.perms.can_be_representative:
                self.roles.add(role)
            elif role.name == 'RCR_EMPLOYEE' and self.perms.can_be_rcr_employee:
                self.roles.add(role)
            else:
                raise Exception(f"User does not have permission to be assigned the {role.name} role.")