from django.contrib import admin


from .models import Court
from .models import Center
from .models import Group
from .models import User
from .models import Booking
from .models import Booking_Status_Field

admin.site.register(Court)
admin.site.register(Center)
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Booking_Status_Field)



# Register your models here.
