from django.db import models

# Create your models here.


USER_PERMISSION_CHOICES = (
        ('ADMIN', 'ADMIN'),
        ('GROUP_MANAGER', 'GROUP MANAGER'),
        ('REGULAR', 'REGULAR'),
        )


class Center(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    lat = models.FloatField()
    lng = models.FloatField()
    numCourts = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return(self.name+" "+self.address)



class Court(models.Model):
    center = models.ForeignKey("Center", on_delete=models.CASCADE)
    courtid = models.IntegerField()

    def __str__(self):
        return(self.center.name+" "+str(self.courtid))


class Group(models.Model):
    center = models.CharField(max_length=100)
    price = models.FloatField()
    members = models.ManyToManyField('User')

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    permission = models.CharField(max_length=15, choices=USER_PERMISSION_CHOICES)
    def __str__(self):
        return(self.name+" "+self.email+" "+self.phone)


class Booking(models.Model):
    center = models.ForeignKey("Center", on_delete=models.CASCADE)
    courts = models.ManyToManyField('Court')
    booking_slot_start = models.DateTimeField()
    booking_slot_end = models.DateTimeField()
    booker = models.ForeignKey("User", on_delete=models.CASCADE)
    group = models.CharField(max_length=100)
    status = models.ForeignKey('Booking_Status_Field', on_delete=models.PROTECT)

    def __str__(self):
        return(self.center.name+" Court "+str(self.courts)+" "+str(self.booking_slot_start)+"-"+str(self.booking_slot_end))
    


class Booking_Status_Field(models.Model):
    booking_status_field_choice=models.CharField(max_length=10)

    def __str__(self):
        return(self.booking_status_field_choice)



