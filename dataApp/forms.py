from django import forms
from .models import UserDetails

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'  # Include all fields from the UserDetails model