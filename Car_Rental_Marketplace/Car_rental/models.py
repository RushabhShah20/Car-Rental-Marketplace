from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import AuthenticationForm
from django.apps import apps
from django.contrib.auth.hashers import check_password


# Create your models here.
class Car_renter(models.Model):
    car_renter_id = models.AutoField((""), primary_key=True)
    phone_number = models.IntegerField((""))
    username = models.CharField((""), max_length=50)
    email = models.CharField((""), max_length=50)
    password = models.CharField((""), max_length=50)


class Orders(models.Model):
    order_id = models.AutoField((""), primary_key=True)
    car_company = models.CharField((""), max_length=50)
    car_model = models.CharField((""), max_length=50)
    rent_start_time = models.TimeField((""), auto_now=False, auto_now_add=False)
    rent_end_time = models.TimeField((""), auto_now=False, auto_now_add=False)
    rent_price = models.IntegerField((""))
