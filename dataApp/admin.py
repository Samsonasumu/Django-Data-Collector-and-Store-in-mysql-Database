from django.contrib import admin
from . models import UserDetails, GroupDetails

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(GroupDetails)