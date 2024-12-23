# Generated by Django 5.1 on 2024-12-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsdetails',
            name='members_female',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sportsdetails',
            name='members_male',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sportsdetails',
            name='year_founded',
            field=models.PositiveIntegerField(blank=True, default=2021),
        ),
    ]
