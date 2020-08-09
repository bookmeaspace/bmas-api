from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound

from .models import *
from .serializers import *
from .filters import *


class getBookingsByUser(viewsets.ModelViewSet):
    serializer_class = getBookingsSerializer
    queryset = Booking.objects.all()
    http_method_names = ['get', 'head']
    ordering_fields=['id']
    filter_backends=(DjangoFilterBackend,)
    filterset_class = bookingsFilterSet

class getUsers(viewsets.ModelViewSet):
    serializer_class = getUsersSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'head']
    ordering_fields=['id']
    filter_backends=(DjangoFilterBackend,)
    filterset_class = usersFilterSet




# Create your views here.
