# Generated by Django 5.1 on 2024-10-31 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('chairperson', models.CharField(default='', max_length=100)),
                ('chairperson_contact', models.CharField(default='', max_length=100)),
                ('chairperson_email', models.EmailField(default='abc@gmail.com', max_length=254)),
                ('secretary', models.CharField(default='', max_length=100)),
                ('secretary_contact', models.CharField(default='', max_length=100)),
                ('secretary_email', models.EmailField(default='abc@gmail.com', max_length=254)),
                ('has_Bank_Account', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('which_bank', models.CharField(default='', max_length=100)),
                ('main_activity', models.CharField(default='', max_length=255)),
                ('any_other_activity', models.CharField(blank=True, default='', max_length=255)),
                ('registration_number', models.CharField(default='', max_length=50, unique=True)),
                ('year_of_registration', models.IntegerField(default=2024)),
                ('sub_county', models.CharField(choices=[('Sabatia', 'Sabatia'), ('Vihiga', 'Vihiga'), ('Luanda', 'Luanda'), ('Emuhaya', 'Emuhaya'), ('Tiriki West', 'Tiriki West'), ('Tiriki East', 'Tiriki East')], max_length=255)),
                ('ward', models.CharField(choices=[('Shiru Ward', 'Shiru Ward'), ('Gisambai Ward', 'Gisambai Ward'), ('Shamakhokho Ward', 'Shamakhokho Ward'), ('Banja Ward', 'Banja Ward'), ('Muhudu Ward', 'Muhudu Ward'), ('Tambua Ward', 'Tambua Ward'), ('Jepkoyai Ward', 'Jepkoyai Ward'), ('Izava-Lyaduywa Ward', 'Izava-Lyaduywa Ward'), ('West Sabatia Ward', 'West Sabatia Ward'), ('Chavakali Ward', 'Chavakali Ward'), ('North Maragoli Ward', 'North Maragoli Ward'), ('Busali Ward', 'Busali Ward'), ('Wodanga Ward', 'Wodanga Ward'), ('Central Bunyore Ward', 'Central Bunyore Ward'), ('North East Bunyore Ward', 'North East Bunyore Ward'), ('West Bunyore Ward', 'West Bunyore Ward'), ('Luanda Township Ward', 'Luanda Township Ward'), ('Luanda South Ward', 'Luanda South Ward'), ('Mwibona Ward', 'Mwibona Ward'), ('Wemilabi Ward', 'Wemilabi Ward'), ('Emabungo Ward', 'Emabungo Ward'), ('Mungoma Ward', 'Mungoma Ward'), ('Central Maragoli Ward', 'Central Maragoli Ward'), ('Lugaga/Wamuluma Ward', 'Lugaga/Wamuluma Ward'), ('South Maragoli Ward', 'South Maragoli Ward')], max_length=255)),
                ('location', models.CharField(default='', max_length=255)),
                ('sub_location', models.CharField(default='', max_length=255)),
                ('village', models.CharField(default='', max_length=255)),
                ('current_county_of_residence', models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Taita/Taveta', 'Taita/Taveta'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('Meru', 'Meru'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ("Murang'a", "Murang'a"), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West Pokot', 'West Pokot'), ('Samburu', 'Samburu'), ('Trans Nzoia', 'Trans Nzoia'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo/Marakwet', 'Elgeyo/Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Migori', 'Migori'), ('Kisii', 'Kisii'), ('Nyamira', 'Nyamira'), ('Nairobi City', 'Nairobi City')], max_length=255)),
                ('are_you_beneficiary_of_any_empowerment_fund', models.CharField(choices=[('youth enterprise development fund', 'Youth enterprise development fund'), ('uwezo fund', 'Uwezo fund'), ('ngaff', 'NGAAF'), ('other', 'other')], max_length=200)),
                ('number_of_members', models.PositiveIntegerField(default=0)),
                ('members_male', models.PositiveIntegerField(default=0)),
                ('members_female', models.PositiveIntegerField(default=0)),
                ('total_members_with_disability', models.PositiveIntegerField(default=0)),
                ('members_18_35', models.PositiveIntegerField(default=0)),
                ('Name_and_phone_number_of_group_members', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='static/')),
                ('video_url', models.URLField(blank=True, default='video')),
                ('photo', models.ImageField(blank=True, upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Middle_name', models.CharField(default='', max_length=50)),
                ('Last_name', models.CharField(default='', max_length=50)),
                ('national_id_number', models.CharField(default='', max_length=20, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=10)),
                ('Do_you_have_Any_disability', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('If_yes_then_which_disability', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=254, unique=True)),
                ('DOB', models.DateTimeField(default='2023-01-15')),
                ('age', models.IntegerField(null=True)),
                ('age_bracket', models.CharField(choices=[('age_0to15', 'age_0to15'), ('age_16to24', 'age_16to24'), ('age_25to34', 'age_25to34'), ('age_35to44', 'age_35to44'), ('age_44andabove', 'age_44andabove')], max_length=100)),
                ('contact', models.CharField(default='+254', max_length=20, unique=True)),
                ('alternative_contact', models.CharField(blank=True, default='+254', max_length=20)),
                ('has_passport', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('sub_county', models.CharField(choices=[('Sabatia', 'Sabatia'), ('Vihiga', 'Vihiga'), ('Luanda', 'Luanda'), ('Emuhaya', 'Emuhaya'), ('Tiriki West', 'Tiriki West'), ('Tiriki East', 'Tiriki East')], max_length=255)),
                ('ward', models.CharField(choices=[('Shiru Ward', 'Shiru Ward'), ('Gisambai Ward', 'Gisambai Ward'), ('Shamakhokho Ward', 'Shamakhokho Ward'), ('Banja Ward', 'Banja Ward'), ('Muhudu Ward', 'Muhudu Ward'), ('Tambua Ward', 'Tambua Ward'), ('Jepkoyai Ward', 'Jepkoyai Ward'), ('Izava-Lyaduywa Ward', 'Izava-Lyaduywa Ward'), ('West Sabatia Ward', 'West Sabatia Ward'), ('Chavakali Ward', 'Chavakali Ward'), ('North Maragoli Ward', 'North Maragoli Ward'), ('Busali Ward', 'Busali Ward'), ('Wodanga Ward', 'Wodanga Ward'), ('Central Bunyore Ward', 'Central Bunyore Ward'), ('North East Bunyore Ward', 'North East Bunyore Ward'), ('West Bunyore Ward', 'West Bunyore Ward'), ('Luanda Township Ward', 'Luanda Township Ward'), ('Luanda South Ward', 'Luanda South Ward'), ('Mwibona Ward', 'Mwibona Ward'), ('Wemilabi Ward', 'Wemilabi Ward'), ('Emabungo Ward', 'Emabungo Ward'), ('Mungoma Ward', 'Mungoma Ward'), ('Central Maragoli Ward', 'Central Maragoli Ward'), ('Lugaga/Wamuluma Ward', 'Lugaga/Wamuluma Ward'), ('South Maragoli Ward', 'South Maragoli Ward')], max_length=255)),
                ('location', models.CharField(default='', max_length=255)),
                ('sub_location', models.CharField(default='', max_length=255)),
                ('village', models.CharField(default='', max_length=255)),
                ('current_county_of_residence', models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Taita/Taveta', 'Taita/Taveta'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('Meru', 'Meru'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ("Murang'a", "Murang'a"), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West Pokot', 'West Pokot'), ('Samburu', 'Samburu'), ('Trans Nzoia', 'Trans Nzoia'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo/Marakwet', 'Elgeyo/Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Migori', 'Migori'), ('Kisii', 'Kisii'), ('Nyamira', 'Nyamira'), ('Nairobi City', 'Nairobi City')], max_length=255)),
                ('professional_Qualification', models.CharField(choices=[('NURSE', 'Nurse'), ('CARE_GIVER', 'Care Giver'), ('HOSPITALITY', 'Hospitality (Chef, Barista, etc.)'), ('SECURITY', 'Security/Manual Labor'), ('DOMESTIC_WORK', 'Domestic Work'), ('TEACHING', 'Teaching (STEM, Subject, Special Ed, ECD)'), ('CAREGIVER_HEALTHCARE_ASSISTANT', 'Caregiver/Healthcare Assistant'), ('SOCIAL_WORK', 'Social Work'), ('ICT', 'ICT'), ('AGRICULTURE', 'Agriculture'), ('BEAUTY', 'Beauty'), ('MECHANIC', 'Mechanic'), ('TRUCK_DRIVER', 'Truck Driver'), ('CAR_DRIVER', 'Small Car to a Canter Vehicle Driver'), ('ACCOUNTANTS', 'Accountants'), ('ECONOMISTS', 'Economists'), ('PROJECT_MANAGERS', 'project managers'), ('OTHER', 'Other')], max_length=50)),
                ('highest_education_level', models.CharField(blank=True, choices=[('UNIVERSITY_DEGREE', 'University Degree'), ('FORM_FOUR_KCSE', 'Form Four KSCE Certificate'), ('DIPLOMA', 'Diploma'), ('CERTIFICATE', 'Certificate'), ('KCPE', 'KCPE'), ('MASTERS', 'Masters')], max_length=20)),
                ('field_of_study', models.CharField(blank=True, max_length=100)),
                ('area_of_specialization', models.CharField(blank=True, max_length=100)),
                ('institution', models.CharField(blank=True, max_length=100)),
                ('graduation_year', models.IntegerField(blank=True, default='2021', null=True)),
                ('additional_skills', models.CharField(max_length=200)),
                ('talent', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('name_of_employer', models.CharField(max_length=200)),
                ('Belong_to_Any_Group', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('group_name', models.CharField(max_length=200)),
                ('belong_to_two_or_more_groups', models.CharField(default='group B, GROUP C', max_length=200)),
                ('Do_you_have_Any_bussiness', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('bussiness_name', models.CharField(max_length=200)),
                ('bussiness_type', models.CharField(max_length=200)),
                ('other_bussiness_type', models.CharField(default='shoe selling, carpentry', max_length=200)),
                ('business_sector', models.CharField(choices=[('Manufacturing', 'Manufacturing'), ('Construction', 'Construction'), ('Processing', 'Processing'), ('Retail', 'Retail'), ('Wholesale', 'Wholesale'), ('Transportation', 'Transportation'), ('Hospitality', 'Hospitality'), ('Finance', 'Finance'), ('Healthcare', 'Healthcare'), ('Education', 'Education'), ('Technology', 'Technology'), ('MPESA', 'MPESA')], max_length=255)),
                ('Are_you_registerd', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=200)),
                ('Registration_number', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
