from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import AuthenticationForm
from django.apps import apps


# Create your models here.
class Car_renter(models.Model):
    phone_number = models.IntegerField((""))
    username = models.CharField((""), max_length=50)
    email = models.CharField((""), max_length=50)
    password = models.CharField((""), max_length=50)
