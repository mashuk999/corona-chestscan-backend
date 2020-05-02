from django.db import models

# Create your models here.
class ResponseModel(models.Model):
    category = models.CharField(max_length=100)
    confidence = models.CharField(max_length=100)

class RequestData(models.Model):
    photo = models.ImageField(upload_to='post_images')