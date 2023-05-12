# Generated by Django 4.2.1 on 2023-05-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("car_company", models.CharField(max_length=50, verbose_name="")),
                ("car_model", models.CharField(max_length=50, verbose_name="")),
                (
                    "date_of_registration",
                    models.CharField(max_length=50, verbose_name=""),
                ),
            ],
        ),
    ]
