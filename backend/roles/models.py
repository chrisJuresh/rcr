from django.db import models

class Role(models.Model):
    """
    Defines various roles available in the system.
    """
    class RoleChoices(models.TextChoices):
        REVIEWER = 'REVIEWER', 'Reviewer'
        REPRESENTATIVE = 'REPRESENTATIVE', 'Representative'
        TRUST_EMPLOYEE = 'TRUST_EMPLOYEE', 'Trust Employee'
        RCR_EMPLOYEE = 'RCR_EMPLOYEE', 'RCR Employee'

    name = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        unique=True,
        verbose_name='Role Name'
    )

    def __str__(self):
        return self.get_name_display()
