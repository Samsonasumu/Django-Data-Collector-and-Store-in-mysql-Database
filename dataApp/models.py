from django.db import models
import datetime

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    #national_id_number = models.CharField(max_length=20, unique=True)  # Assuming unique ID numbers
    
    has_passport = models.BooleanField(default=False)
    location = models.CharField(max_length=255, default="Vihiga County")

    
    occupation = models.CharField(max_length=200)
    location = models.CharField(max_length=255, default="ee")  # Add a default value (empty string)
    email = models.EmailField(default="ee")
    file = models.FileField(upload_to='documents/', default="ee")
    # Academic details
    highest_qualification = models.CharField(max_length=100, blank=True)
    field_of_study = models.CharField(max_length=100, blank=True)

    # Economic activities
    industry = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class GroupDetails(models.Model):
    group_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    #registration_number = models.CharField(max_length=50, unique=True)  # Assuming unique registration numbers
    #year_of_registration = models.IntegerField(default="none")  # Set default to current year
    year_of_registration = models.IntegerField(default=datetime.date.today().year)  # Set default to current year

    nature_of_activity = models.CharField(max_length=255, default="Unknown")  # Provide a default value

    ward = models.CharField(max_length=100, default="Unknown")  # Provide a default value
    name_of_contact_person = models.CharField(max_length=255, default="Unknown")
    contact = models.CharField(max_length=20, default="Unknown")  # Adjust for phone number format
    email = models.EmailField(default="unknown@example.com")  # Provide a default email
    number_of_members = models.IntegerField(default=0)
    members_male = models.IntegerField(default=0)
    members_female = models.IntegerField(default=0)
    members_18_35 = models.IntegerField(default=0)

    def __str__(self):
        return self.group_name