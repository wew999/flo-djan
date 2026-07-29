from django.db import models

class logData(models.Model):
    username =  models.CharField(max_length=30)
    password = models.CharField(max_length=30, )

class orderData(models.Model):
    user =  models.ForeignKey(logData, on_delete = models.CASCADE)
    order = models.JSONField()
    address = models.CharField(max_length=100, blank=True)
# Create your models here.
