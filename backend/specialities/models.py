from django.db import models

class ConsultantType(models.Model):
    class ConsultantChoices(models.TextChoices):
        RADIOLOGY = 'RADIOLOGY', 'Radiology'
        ONCOLOGY = 'ONCOLOGY', 'Oncology'

    name = models.CharField(
        max_length=20,
        choices=ConsultantChoices.choices,
        unique=True,
        verbose_name='Role Name'
    )

    def __str__(self):
        return self.get_name_display()


class Speciality(models.Model):
    name = models.CharField(max_length=100)
    consultant_type = models.ForeignKey(ConsultantType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.consultant_type.name} - {self.name}"

        