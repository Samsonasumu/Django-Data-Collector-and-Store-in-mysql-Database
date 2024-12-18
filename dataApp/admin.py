from django.contrib import admin
from . models import UserDetails, GroupDetails, Image, SportsDetails

from .models import UpcomingProgram

admin.site.register(UpcomingProgram)
 # Register your models here.
admin.site.register(UserDetails)

admin.site.register(GroupDetails)
admin.site.register(Image)
admin.site.register(SportsDetails)

