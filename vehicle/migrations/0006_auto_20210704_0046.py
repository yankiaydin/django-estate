# Generated by Django 3.2.4 on 2021-07-03 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0005_alter_rentcarphoto_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="forsalecar",
            name="pics_of_car",
        ),
        migrations.AlterField(
            model_name="forsalecar",
            name="fuel",
            field=models.CharField(
                choices=[
                    ("Oil", "Oil"),
                    ("Diesel", "Diesel"),
                    ("LPG", "LPG"),
                    ("Hybrid", "Hybrid"),
                ],
                max_length=20,
                verbose_name="Fuel",
            ),
        ),
        migrations.AlterField(
            model_name="rentcarphoto",
            name="images",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="rentalcar/",
                verbose_name="Upload Images",
            ),
        ),
        migrations.CreateModel(
            name="SaleCarPhoto",
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
                        blank=True,
                        null=True,
                        upload_to="forsalecar/",
                        verbose_name="Upload Images",
                    ),
                ),
                (
                    "post",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicle.forsalecar",
                    ),
                ),
            ],
        ),
    ]
