from django.db import models
from django.contrib.auth.models import User

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.CharField(max_length=100)
    # Add any extra fields specific to the admin
    def __str__(self):
        return self.user.username

# Create your models here.
