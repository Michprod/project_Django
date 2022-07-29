from turtle import onrelease
from django.db import models
from django.contrib.auth.models import User
from film.models import Film


# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to = 'profile_pics',default='default.jpg') 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    films = models.ManyToManyField(Film)
  