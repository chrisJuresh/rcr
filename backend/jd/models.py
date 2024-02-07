from django.db import models

class JD(models.Model):
    document = models.FileField(upload_to='jd_documents/')
    submission_date = models.DateTimeField(auto_now_add=True)