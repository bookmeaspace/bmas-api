from django_filters import rest_framework


class bookingsFilterSet(rest_framework.FilterSet):
    id = rest_framework.RangeFilter()
    class Meta:
        fields= ('id')


class usersFilterSet(rest_framework.FilterSet):
    id = rest_framework.RangeFilter()
    class Meta:
        fields= ('id')




