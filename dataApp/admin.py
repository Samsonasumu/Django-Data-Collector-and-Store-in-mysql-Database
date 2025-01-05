from django.contrib import admin
from . models import GroupDetails, UpcomingProgram, SportsDetails, Person, Business
from django import forms

class BusinessForm(forms.ModelForm):
    # Use CKEditor widget for the description field in the admin
    description = forms.CharField()

    class Meta:
        model = Business
        fields = '__all__'

class BusinessAdmin(admin.ModelAdmin):
    form = BusinessForm

admin.site.register(Person)
admin.site.register(Business, BusinessAdmin)
admin.site.register(GroupDetails)
admin.site.register(SportsDetails)
admin.site.register(UpcomingProgram)
