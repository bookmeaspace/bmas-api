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

    def __str__(self):
        return(self.center+" "+str(self.courtid))


class Group(models.Model):
    center = models.CharField(max_length=100)
    price = models.FloatField()
    members = models.ManyToManyField('User')

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    permission = models.CharField(max_length=100)

class Booking(models.Model):
    center = models.CharField(max_length=100)
    courts = models.ManyToManyField('Court')
    booking_slot_start = models.DateTimeField()
    booking_slot_end = models.DateTimeField()
    booker = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    status = models.ManyToManyField('Booking_Status_Field')

    def __str__(self):
        return(self.center+" Court "+str(self.courts)+" "+str(self.booking_slot_start)+"-"+str(self.booking_slot_end))

class Booking_Status_Field(models.Model):
    booking_status_field_choice=models.CharField(max_length=10)

    def __str__(self):
        return(self.booking_status_field_choice)





