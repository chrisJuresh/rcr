from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 

class Trust(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 