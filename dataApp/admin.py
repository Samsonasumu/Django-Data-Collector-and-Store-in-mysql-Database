from django.contrib import admin
from . models import UserDetails, GroupDetails

from .models import UpcomingProgram

admin.site.register(UpcomingProgram)
 # Register your models here.
admin.site.register(UserDetails)
admin.site.register(GroupDetails)