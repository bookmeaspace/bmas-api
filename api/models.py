from django.db import models

# Create your models here.

class Center(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    lat = models.FloatField()
    lng = models.FloatField()
    numCourts = models.IntegerField()

class Court(models.Model):
    center = models.CharField(max_length=100)
    courtid = models.IntegerField()

class Group(models.Model):
    center = models.CharField(max_length=100)
    price = models.FloatField()
    members = models.ManyToManyField('User')

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    
class Booking(models.Model):
    center = models.CharField(max_length=100)
    courts = models.ManyToManyField('Court')
    date = models.IntegerField()
    time = models.IntegerField()
    booker = models.CharField(max_length=100)
    group = models.CharField(max_length=100, null=True)
    status = models.IntegerField()

