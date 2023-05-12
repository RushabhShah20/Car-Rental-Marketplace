from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.


class Car_leaser(models.Model):
    car_owner_name = models.CharField((""), max_length=50)
    car_owner_email = models.EmailField((""), max_length=254)
    car_owner_mobile_number = models.IntegerField((""))
    car_owner_car_company = models.CharField((""), max_length=50)
    car_owner_car_model = models.CharField((""), max_length=50)
