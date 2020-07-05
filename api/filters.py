from django_filters import rest_framework
from .models import *



class bookingsFilterSet(rest_framework.FilterSet):
    userEmail = rest_framework.ModelChoiceFilter(field_name="booker", to_field_name="email", queryset=User.objects.all())
    
    class Meta:
        model = Booking
        fields= ('userEmail', )

class usersFilterSet(rest_framework.FilterSet):
    id = rest_framework.RangeFilter()
    class Meta:
        fields= ('id')



