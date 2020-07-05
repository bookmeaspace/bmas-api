from rest_framework import serializers
from .models import *

class getBookingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking 
        fields = ("center", "courts", "booking_slot_start", "booking_slot_end", "booker", "group", "status",) 
class getUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =User
        fields= ("name", "email", "phone", "password", "permission",) 

