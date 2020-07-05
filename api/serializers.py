from rest_framework import serializers
from .models import *

class getUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =User
        fields= ("name", "email", "phone", "password", "permission",) 

class getUsersWithoutPasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =User
        fields= ("name", "email", "phone", "permission",) 

class getCenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Center
        fields= ("name", "address", "lat", "lng", "numCourts", "price") 

class getStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Booking_Status_Field
        fields=("booking_status_field_choice",)

class getBookingsSerializer(serializers.HyperlinkedModelSerializer):
    # Booking_Center = serializers.ReadOnlyField()
#     Booking_Email = serializers.ReadOnlyField()
#     Booking_Court_id = serializers.ReadOnlyField()
    booker = getUsersSerializer()
    center = getCenterSerializer()
    status = getStatusSerializer()
    class Meta:
        model = Booking 
        fields= ("booker", "center", "booking_slot_start", "booking_slot_end", "status")


