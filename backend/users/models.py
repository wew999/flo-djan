from django.db import models

class logData(models.Model):
    username =  models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address =  models.CharField(max_length=30)

class orderData(models.Model):
    username =  models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address =  models.CharField(max_length=30)
# Create your models here.
