from django.db import models

# Create your models here.
class ResponseModel(models.Model):
    category = models.CharField(max_length=100)
    confidence = models.CharField(max_length=100)