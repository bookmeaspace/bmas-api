from django.urls import path, include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()

router.register(r'getBookingsByUser', views.getBookingsByUser, basename='getBookingsByUser')
router.register(r'getUsers', views.getUsers, basename='getUsers')


urlpatterns = router.urls
