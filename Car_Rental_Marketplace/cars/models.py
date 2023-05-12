from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.


class Car(models.Model):
    state_choice = (
        ("AP", "Andhra Pradesh"),
        ("AR", "Arunachal Pradesh"),
        ("AS", "Assam"),
        ("BR", "Bihar"),
        ("CG", "Chattisgarh"),
        ("GA", "Goa"),
        ("GJ", "Gujarat"),
        ("HR", "Harayana"),
        ("HP", "Himachal Pradesh"),
        ("JH", "Jharkhand"),
        ("KA", "Karnataka"),
        ("KL", "Kerela"),
        ("MP", "Madhya Pradesh"),
        ("MH", "Maharashtra"),
        ("MN", "Manipur"),
        ("ML", "Meghalaya"),
        ("MZ", "Mizoram"),
        ("NL", "Nagaland"),
        ("OD", "Odisha"),
        ("PB", "Punjab"),
        ("RJ", "Rajasthan"),
        ("SK", "Sikkim"),
        ("TN", "Tamil Nadu"),
        ("TS", "Telangana"),
        ("TR", "Tripura"),
        ("UP", "Uttar Pradesh"),
        ("UK", "Uttarakhand"),
        ("WB", "West Bengal"),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    car_company = models.CharField(
        (""),
        max_length=50,
    )
    car_id = models.AutoField((""), primary_key=True)
    car_model = models.CharField(max_length=50)
    date_of_registration = models.CharField(max_length=50)
    car_price = models.IntegerField()
    car_registration_state = models.CharField((""), max_length=50)
