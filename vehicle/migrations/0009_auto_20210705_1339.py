# Generated by Django 3.2.4 on 2021-07-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0008_alter_rentcarphoto_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rentalcar",
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
            field=models.ImageField(blank=True, null=True, upload_to="rentalcars/"),
        ),
        migrations.AlterField(
            model_name="salecarphoto",
            name="images",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="forsalecars/",
                verbose_name="Upload Images",
            ),
        ),
    ]
