# Generated by Django 3.2.4 on 2021-07-02 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0002_auto_20210702_1207"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rentalcar",
            name="pics_of_car",
        ),
        migrations.CreateModel(
            name="RentCarPhoto",
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
                (
                    "images",
                    models.ImageField(
                        blank=True, upload_to="rentalcar/", verbose_name="Upload Images"
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicle.rentalcar",
                    ),
                ),
            ],
        ),
    ]