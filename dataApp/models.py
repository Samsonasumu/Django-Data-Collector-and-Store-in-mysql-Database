from django.db import models
import datetime
from django.core.validators import MinValueValidator


class UserDetails(models.Model):
    first_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=50, default="")
    national_id_number = models.CharField(max_length=20, unique=True, default="")  # Unique identifier for patient
    gender = models.CharField(max_length=10, choices=(
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ), blank=True)
    email = models.EmailField(default="abc@gmail.com")
    DOB = models.DateTimeField(default="2023-01-15")
    #age = 
    talent = models.CharField(max_length=200)

 
    
    
    area_of_specialization = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=20, default="")  # Contact information for doctor
    has_passport = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])

    PASSPORT_NUMBER = models.CharField(max_length=20, blank=True)  # Optional passport number
    talent = models.CharField(max_length=200)
    additional_skills = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    name_of_employer = models.CharField(max_length=200)
    
    
    sub_county = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    location = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    sub_location = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    ward = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    village = models.CharField(max_length=255, default="")  # Add a default value (empty string)


    
    # Academic details
    # Education Details
    highest_education_level = models.CharField(
        max_length=20,
        choices=(
            ('UNIVERSITY_DEGREE', 'University Degree'),
            ('FORM_FOUR_KCSE', 'Form Four KSCE Certificate'),
            ('DIPLOMA', 'Diploma'),
            ('CERTIFICATE', 'Certificate'),
            ('KCPE', 'KCPE'),
            ('MASTERS', 'Masters'),
        ), blank = True
    )
    field_of_study = models.CharField(max_length=100, blank=True)
    area_of_specialization = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    graduation_year = models.IntegerField(blank=True, null=True, default="2021")
    #relevant_certifications = models.FileField(upload_to='documents/', default="")

    
    
    
    # Profession Details
    profession = models.CharField(max_length=50, choices=(
        ('NURSE', 'Nurse'),
        ('CARE_GIVER', 'Care Giver'),
        ('HOSPITALITY', 'Hospitality (Chef, Barista, etc.)'),
        ('SECURITY', 'Security/Manual Labor'),
        ('DOMESTIC_WORK', 'Domestic Work'),
        ('TEACHING', 'Teaching (STEM, Subject, Special Ed, ECD)'),
        ('CAREGIVER_HEALTHCARE_ASSISTANT', 'Caregiver/Healthcare Assistant'),
        ('SOCIAL_WORK', 'Social Work'),
        ('ICT', 'ICT'),
        ('AGRICULTURE', 'Agriculture'),
        ('BEAUTY', 'Beauty'),
        ('MECHANIC', 'Mechanic'),
        ('TRUCK_DRIVER', 'Truck Driver'),
        ('CAR_DRIVER', 'Small Car to a Canter Vehicle Driver'),
        ('ACCOUNTANTS','Accountants'),
        ('ECONOMISTS','Economists'),
        ('PROJECT_MANAGERS','project managers'),
        ('OTHER', 'Other'),
    ), blank = False)
    
    
    Any_disability = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    disability_true = models.CharField(max_length=200, blank=True)


    Belong_to_aGroup = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    group_name = models.CharField(max_length=200)
    
    Do_you_have_Any_bussiness = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    bussiness_name = models.CharField(max_length=200)
    bussiness_type = models.CharField(max_length=200)
    Are_you_registerd = models.CharField(max_length=200, choices=[('yes', 'Yes'), ('no', 'No')])
    Registration_number = models.CharField(max_length=200)

    agrees_to_data_protection = models.BooleanField(default=False)



    # Economic activities
 
    def __str__(self):
        return self.first_name


class GroupDetails(models.Model):
    group_name = models.CharField(max_length=100)
    chairperson = models.CharField(max_length=100, default="")    
    chairperson_contact = models.CharField(max_length=100, default="")
    chairperson_email = models.EmailField(default="abc@gmail.com")

    secretary = models.CharField(max_length=100, default="")    
    secretary_contact = models.CharField(max_length=100, default="")
    secretary_email = models.EmailField(default="abc@gmail.com")



    has_Bank_Account = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    which_bank = models.CharField(max_length=100, default="")

    
    
    
    main_activity = models.CharField(max_length=255, default="")  # Provide a default value
    any_other_activity = models.CharField(max_length=255, default="", blank=True)  # Provide a default value
    registration_number = models.CharField(max_length=50, unique=True, default="")  # Assuming unique registration numbers
    #year_of_registration = models.IntegerField(default="none")  # Set default to current year
    year_of_registration = models.IntegerField(default=datetime.date.today().year)  # Set default to current year




    sub_county = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    location = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    sub_location = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    ward = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    village = models.CharField(max_length=255, default="")  # Add a default value (empty string)



     
    are_you_beneficiary_of_fund = models.CharField(max_length=200, 
    choices=[('youth enterprise development fund', 'Youth enterprise development fund'),
     ('uwezo fund', 'Uwezo fund'),
      ('ngaff', 'NGAAF')])


    number_of_members = models.IntegerField(default=0)
    members_male = models.IntegerField(default=0)
    members_female = models.IntegerField(default=0)
    members_18_35 = models.IntegerField(default=0)

    agrees_to_data_protection = models.BooleanField(default=False)


    def __str__(self):
        return self.group_name