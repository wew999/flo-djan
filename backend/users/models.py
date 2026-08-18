from django.db import models

class logData(models.Model):
    username =  models.CharField(max_length=30)
    password = models.CharField(max_length=30 )
    isAdmin = models.CharField(max_length=30, blank=True )

class orderData(models.Model):
    user =  models.ForeignKey(logData, on_delete = models.CASCADE)
    order = models.CharField(max_length=100)
    identifier =  models.IntegerField()
    address = models.CharField(max_length=100, blank=True)

class myProductionData(models.Model):
    heading = models.CharField(max_length=40)
    info = models.CharField(max_length=1000)
    price =  models.IntegerField()
# Create your models here.
