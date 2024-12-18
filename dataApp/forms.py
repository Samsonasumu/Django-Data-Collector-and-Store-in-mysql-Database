from django import forms
from .models import UserDetails, GroupDetails, SportsDetails
from django.forms import ModelForm, TextInput, EmailInput

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'  # Include all fields from the UserDetails model
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                })
        }
class GroupDetailsForm(forms.ModelForm):
    class Meta:
        model = GroupDetails
        fields = '__all__'  # Include all fields from the UserDetails model


        
class SportsDetailsForm(forms.ModelForm):
    class Meta:
        model = SportsDetails
        fields = '__all__'  # Include all fields from the UserDetails model


   