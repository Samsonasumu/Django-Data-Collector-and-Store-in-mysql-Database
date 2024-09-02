from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=200)
    location = models.CharField(max_length=255, default="ee")  # Add a default value (empty string)
    email = models.EmailField()
    file = models.FileField(upload_to='documents/')
    saved_time = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.name