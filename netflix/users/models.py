from turtle import onrelease
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to = 'profile_pics',default='default.jpg') 
    user = models.OneToOneField(User,on_delete=models.CASCADE)

  