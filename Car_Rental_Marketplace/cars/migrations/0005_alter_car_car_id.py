# Generated by Django 4.2.1 on 2023-05-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0004_remove_car_id_car_car_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_id",
            field=models.AutoField(primary_key=True, serialize=False, verbose_name=""),
        ),
    ]
