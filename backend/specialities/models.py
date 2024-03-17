from django.db import models

class ConsultantType(models.Model):
    CONSULTANT = (
        ('RADIOLOGY', 'Radiologist'),
        ('ONCOLOGY', 'Oncologist')
    )

    name = models.CharField(max_length=20, choices=CONSULTANT, unique=True)

    def __str__(self):
        return self.name

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    consultant_type = models.ForeignKey(ConsultantType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.consultant_type.name} - {self.name}"