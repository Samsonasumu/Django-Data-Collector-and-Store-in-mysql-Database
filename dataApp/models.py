from django.db import models
import datetime
from django.core.validators import MinValueValidator


class UserDetails(models.Model):
    First_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=50, default="")
    Last_name = models.CharField(max_length=50, default="")
    national_id_number = models.CharField(max_length=20, unique=True, default="")  # Unique identifier for patient
    gender = models.CharField(max_length=10, choices=(
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ), blank=True)
        
    Do_you_have_Any_disability = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    If_yes_then_which_disability = models.CharField(max_length=200, blank=True)


    email = models.EmailField(default="abc@gmail.com", unique=True)
    DOB = models.DateTimeField(default="2023-01-15")
    age = models.IntegerField(blank=False, null=True, )
    age_bracket = models.CharField(max_length=100, choices=[('age_0to15', 'age_0to15'),
     ('age_16to24', 'age_16to24'), ('age_25to34','age_25to34'), ('age_35to44','age_35to44'), ("age_44andabove","age_44andabove")])  
   
    contact = models.CharField(max_length=20, default="+254", unique=True)  # Contact information for doctor
    alternative_contact = models.CharField(max_length=20, default="+254",blank=True)  # Contact information for doctor
    has_passport = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])

    
    
    
    sub_county = models.CharField(max_length=255, choices=[('Sabatia','Sabatia'), ('Vihiga','Vihiga'),
     ('Luanda', 'Luanda'), ('Emuhaya', 'Emuhaya'),('Tiriki West','Tiriki West'),('Tiriki East','Tiriki East')])  # Add a default value (empty string)
    
    ward = models.CharField(max_length=255, choices=[('Shiru Ward', 'Shiru Ward'), 
                                                        ('Gisambai Ward', 'Gisambai Ward'), 
                                                        ('Shamakhokho Ward', 'Shamakhokho Ward'), 
                                                        ('Banja Ward', 'Banja Ward'), 
                                                        ('Muhudu Ward', 'Muhudu Ward'), 
                                                        ('Tambua Ward', 'Tambua Ward'), 
                                                        ('Jepkoyai Ward', 'Jepkoyai Ward'), 
                                                        ('Lyaduywa/Izava Ward', 'Lyaduywa/Izava Ward'), 
                                                        ('Sabatia West Ward', 'Sabatia West Ward'), 
                                                        ('Chavakali Ward', 'Chavakali Ward'), 
                                                        ('North Maragoli Ward', 'North Maragoli Ward'), 
                                                        ('Busali Ward', 'Busali Ward'), 
                                                        ('Wodanga Ward', 'Wodanga Ward'), 
                                                        ('Central Bunyore Ward', 'Central Bunyore Ward'), 
                                                        ('North East Bunyore Ward', 'North East Bunyore Ward'), 
                                                        ('West Bunyore Ward', 'West Bunyore Ward'), 
                                                        ('Luanda Township Ward', 'Luanda Township Ward'), 
                                                        ('Luanda South Ward', 'Luanda South Ward'), 
                                                        ('Mwibona Ward', 'Mwibona Ward'), 
                                                        ('Wemilabi Ward', 'Wemilabi Ward'), 
                                                        ('Emabungo Ward', 'Emabungo Ward'), 
                                                        ('Mungoma Ward', 'Mungoma Ward'), 
                                                        ('Maragoli Central Ward', 'Maragoli Central Ward'), 
                                                        ('Lugaga/Wamuluma Ward', 'Lugaga/Wamuluma Ward'), 
                                                        ('Maragoli South Ward', 'Maragoli South Ward')])
    location = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    sub_location = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    village = models.CharField(max_length=255, default="")  # Add a default value (empty string)

    COUNTY_CHOICES = [
    ('Mombasa', 'Mombasa'),
    ('Kwale', 'Kwale'),
    ('Kilifi', 'Kilifi'),
    ('Tana River', 'Tana River'),
    ('Lamu', 'Lamu'),
    ('Taita/Taveta', 'Taita/Taveta'),
    ('Garissa', 'Garissa'),
    ('Wajir', 'Wajir'),
    ('Mandera', 'Mandera'),
    ('Marsabit', 'Marsabit'),
    ('Isiolo', 'Isiolo'),
    ('Meru', 'Meru'),
    ('Tharaka-Nithi', 'Tharaka-Nithi'),
    ('Embu', 'Embu'),
    ('Kitui', 'Kitui'),
    ('Machakos', 'Machakos'),
    ('Makueni', 'Makueni'),
    ('Nyandarua', 'Nyandarua'),
    ('Nyeri', 'Nyeri'),
    ('Kirinyaga', 'Kirinyaga'),
    ('Murang\'a', 'Murang\'a'),
    ('Kiambu', 'Kiambu'),
    ('Turkana', 'Turkana'),
    ('West Pokot', 'West Pokot'),
    ('Samburu', 'Samburu'),
    ('Trans Nzoia', 'Trans Nzoia'),
    ('Uasin Gishu', 'Uasin Gishu'),
    ('Elgeyo/Marakwet', 'Elgeyo/Marakwet'),
    ('Nandi', 'Nandi'),
    ('Baringo', 'Baringo'),
    ('Laikipia', 'Laikipia'),
    ('Nakuru', 'Nakuru'),
    ('Narok', 'Narok'),
    ('Kajiado', 'Kajiado'),
    ('Kericho', 'Kericho'),
    ('Bomet', 'Bomet'),
    ('Kakamega', 'Kakamega'),
    ('Vihiga', 'Vihiga'),
    ('Bungoma', 'Bungoma'),
    ('Busia', 'Busia'),
    ('Siaya', 'Siaya'),
    ('Kisumu', 'Kisumu'),
    ('Homa Bay', 'Homa Bay'),
    ('Migori', 'Migori'),
    ('Kisii', 'Kisii'),
    ('Nyamira', 'Nyamira'),
    ('Nairobi City', 'Nairobi City'),
]
     
    current_county_of_residence = models.CharField(max_length=255, choices=COUNTY_CHOICES)

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
    # Profession Details
    professional_Qualification = models.CharField(max_length=50, choices=(
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

    talent = models.CharField(max_length=200)
    additional_skills = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    name_of_employer = models.CharField(max_length=200)

    field_of_study = models.CharField(max_length=100, blank=True)
    area_of_specialization = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    graduation_year = models.IntegerField(blank=True, null=True, default="2021")
    #relevant_certifications = models.FileField(upload_to='documents/', default="")

    


    Belong_to_Any_Group = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    group_name = models.CharField(max_length=200)
    belong_to_two_or_more_groups = models.CharField(max_length=200, default="group B, GROUP C")

    
    Do_you_have_Any_bussiness = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    bussiness_name = models.CharField(max_length=200)
    bussiness_type = models.CharField(max_length=200)
    other_bussiness_type = models.CharField(max_length=200, default="shoe selling, carpentry")


    BUSINESS_SECTOR_CHOICES = [
    ('Manufacturing', 'Manufacturing'),
    ('Construction', 'Construction'),
    ('Processing', 'Processing'),
    ('Retail', 'Retail'),
    ('Wholesale', 'Wholesale'),
    ('Transportation', 'Transportation'),
    ('Hospitality', 'Hospitality'),
    ('Finance', 'Finance'),
    ('Healthcare', 'Healthcare'),
    ('Education', 'Education'),
    ('Technology', 'Technology'),
    ('MPESA', 'MPESA'),
]
    business_sector = models.CharField(max_length=255, choices=BUSINESS_SECTOR_CHOICES)
    Are_you_registerd = models.CharField(max_length=200, choices=[('yes', 'Yes'), ('no', 'No')])
    Registration_number = models.CharField(max_length=200, unique=True)

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
    sub_county = models.CharField(max_length=255, choices=[('Sabatia','Sabatia'), ('Vihiga','Vihiga'),
     ('Luanda', 'Luanda'), ('Emuhaya', 'Emuhaya'),('Tiriki West','Tiriki West'),('Tiriki East','Tiriki East')])  # Add a default value (empty string)
    

    ward = models.CharField(max_length=255, choices=[('Shiru Ward', 'Shiru Ward'), 
                                                        ('Gisambai Ward', 'Gisambai Ward'), 
                                                        ('Shamakhokho Ward', 'Shamakhokho Ward'), 
                                                        ('Banja Ward', 'Banja Ward'), 
                                                        ('Muhudu Ward', 'Muhudu Ward'), 
                                                        ('Tambua Ward', 'Tambua Ward'), 
                                                        ('Jepkoyai Ward', 'Jepkoyai Ward'), 
                                                        ('Lyaduywa/Izava Ward', 'Lyaduywa/Izava Ward'), 
                                                        ('Sabatia West Ward', 'Sabatia West Ward'), 
                                                        ('Chavakali Ward', 'Chavakali Ward'), 
                                                        ('North Maragoli Ward', 'North Maragoli Ward'), 
                                                        ('Busali Ward', 'Busali Ward'), 
                                                        ('Wodanga Ward', 'Wodanga Ward'), 
                                                        ('Central Bunyore Ward', 'Central Bunyore Ward'), 
                                                        ('North East Bunyore Ward', 'North East Bunyore Ward'), 
                                                        ('West Bunyore Ward', 'West Bunyore Ward'), 
                                                        ('Luanda Township Ward', 'Luanda Township Ward'), 
                                                        ('Luanda South Ward', 'Luanda South Ward'), 
                                                        ('Mwibona Ward', 'Mwibona Ward'), 
                                                        ('Wemilabi Ward', 'Wemilabi Ward'), 
                                                        ('Emabungo Ward', 'Emabungo Ward'), 
                                                        ('Mungoma Ward', 'Mungoma Ward'), 
                                                        ('Maragoli Central Ward', 'Maragoli Central Ward'), 
                                                        ('Lugaga/Wamuluma Ward', 'Lugaga/Wamuluma Ward'), 
                                                        ('Maragoli South Ward', 'Maragoli South Ward')])
    location = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    sub_location = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    village = models.CharField(max_length=255, default="")  # Add a default value (empty string)
    COUNTY_CHOICES = [
    ('Mombasa', 'Mombasa'),
    ('Kwale', 'Kwale'),
    ('Kilifi', 'Kilifi'),
    ('Tana River', 'Tana River'),
    ('Lamu', 'Lamu'),
    ('Taita/Taveta', 'Taita/Taveta'),
    ('Garissa', 'Garissa'),
    ('Wajir', 'Wajir'),
    ('Mandera', 'Mandera'),
    ('Marsabit', 'Marsabit'),
    ('Isiolo', 'Isiolo'),
    ('Meru', 'Meru'),
    ('Tharaka-Nithi', 'Tharaka-Nithi'),
    ('Embu', 'Embu'),
    ('Kitui', 'Kitui'),
    ('Machakos', 'Machakos'),
    ('Makueni', 'Makueni'),
    ('Nyandarua', 'Nyandarua'),
    ('Nyeri', 'Nyeri'),
    ('Kirinyaga', 'Kirinyaga'),
    ('Murang\'a', 'Murang\'a'),
    ('Kiambu', 'Kiambu'),
    ('Turkana', 'Turkana'),
    ('West Pokot', 'West Pokot'),
    ('Samburu', 'Samburu'),
    ('Trans Nzoia', 'Trans Nzoia'),
    ('Uasin Gishu', 'Uasin Gishu'),
    ('Elgeyo/Marakwet', 'Elgeyo/Marakwet'),
    ('Nandi', 'Nandi'),
    ('Baringo', 'Baringo'),
    ('Laikipia', 'Laikipia'),
    ('Nakuru', 'Nakuru'),
    ('Narok', 'Narok'),
    ('Kajiado', 'Kajiado'),
    ('Kericho', 'Kericho'),
    ('Bomet', 'Bomet'),
    ('Kakamega', 'Kakamega'),
    ('Vihiga', 'Vihiga'),
    ('Bungoma', 'Bungoma'),
    ('Busia', 'Busia'),
    ('Siaya', 'Siaya'),
    ('Kisumu', 'Kisumu'),
    ('Homa Bay', 'Homa Bay'),
    ('Migori', 'Migori'),
    ('Kisii', 'Kisii'),
    ('Nyamira', 'Nyamira'),
    ('Nairobi City', 'Nairobi City'),
]
    current_county_of_residence = models.CharField(max_length=255, choices=COUNTY_CHOICES)

    are_you_beneficiary_of_any_empowerment_fund = models.CharField(max_length=200, 
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