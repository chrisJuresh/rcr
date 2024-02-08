from django.db import models

class ConsultantType(models.TextChoices):
    RADIOLOGY = 'Radiology', 'Radiology'
    ONCOLOGY = 'Oncology', 'Oncology'

class Specialty(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=ConsultantType.choices)

    def __str__(self):
        return f"{self.type} - {self.name}"


# class Radiologist(ConsultantBase):
#     SPECIALITY_CHOICES = (
#         ('General', 'General'),
#         ('Breast', 'Breast'),
#         ('Cardiac', 'Cardiac'),
#         ('Chest & Lung', 'Chest & Lung'),
#         ('Cross Sectional Imaging', 'Cross Sectional Imaging'),
#         ('Endocrine radiology', 'Endocrine radiology'),
#         ('Dental/Maxillo-facial', 'Dental/Maxillo-facial'),
#         ('Forensic', 'Forensic'),
#         ('Gastrointestinal', 'Gastrointestinal'),
#         ('Head & Neck', 'Head & Neck'),
#         ('Imaging IT Radiology', 'Imaging IT Radiology'),
#         ('Interventional (inc. Vascular)', 'Interventional (inc. Vascular)'),
#         ('Interventional (non-Vascular)', 'Interventional (non-Vascular)'),
#         ('Medical Education', 'Medical Education'),
#         ('Musculoskeletal', 'Musculoskeletal'),
#         ('Neuroradiology - mainly diagnostic', 'Neuroradiology - mainly diagnostic'),
#         ('Neuroradiology - mainly interventional', 'Neuroradiology - mainly interventional'),
#         ('Obstetric/Gynaecology', 'Obstetric/Gynaecology'),
#         ('Oncological', 'Oncological'),
#         ('Paediatric', 'Paediatric'),
#         ('Paediatric Neuroradiology', 'Paediatric Neuroradiology'),
#         ('PET CT', 'PET CT'),
#         ('Radionuclide', 'Radionuclide'),
#         ('Research', 'Research'),
#         ('Trauma', 'Trauma'),
#         ('Uroradiology', 'Uroradiology'),
#         ('Other', 'Other'),
#     )
#     pass

# class Oncologist(ConsultantBase):
#     SPECIALITY_CHOICES = (
#         ('General', 'General'),
#         ('Acute Oncology', 'Acute Oncology'),
#         ('Breast', 'Breast'),
#         ('CNS/Neuro', 'CNS/Neuro'),
#         ('Colorectal', 'Colorectal'),
#         ('Genitourinary', 'Genitourinary'),
#         ('Gynaecology', 'Gynaecology'),
#         ('Haematological maglignancy', 'Haematological malignancy'),
#         ('Head & Neck', 'Head & Neck'),
#         ('Lung', 'Lung'),
#         ('Paediatric', 'Paediatric'),
#         ('Sarcomas', 'Sarcomas'),
#         ('Skin', 'Skin'),
#         ('Teen & Young adult', 'Teen & Young adult'),
#         ('Thyroid', 'Thyroid'),
#         ('Upper GI (including HPB)', 'Upper GI (including HPB)'),
#         ('Other', 'Other'),
#     )
#     pass