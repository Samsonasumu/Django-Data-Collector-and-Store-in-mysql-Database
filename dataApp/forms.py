from django import forms
from .models import GroupDetails, SportsDetails, Person, Business
from django.forms import ModelForm, TextInput, EmailInput

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = Person
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


class PersonForm(forms.ModelForm):
  class Meta:
    model = Person
    fields = '__all__'

class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = '__all__'


