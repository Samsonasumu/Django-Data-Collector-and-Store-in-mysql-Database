# Generated by Django 5.1 on 2024-09-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0003_userdetails_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(default='ee', max_length=254),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='field_of_study',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='file',
            field=models.FileField(default='ee', upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='highest_qualification',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='industry',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]