# Generated by Django 4.2.1 on 2023-05-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car_renter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone_number", models.IntegerField(verbose_name="")),
                ("username", models.CharField(max_length=50, verbose_name="")),
                ("email", models.CharField(max_length=50, verbose_name="")),
                ("password", models.CharField(max_length=50, verbose_name="")),
            ],
        ),
    ]