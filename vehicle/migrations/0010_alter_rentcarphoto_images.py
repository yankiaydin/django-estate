# Generated by Django 3.2.4 on 2021-07-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0009_auto_20210705_1339"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rentcarphoto",
            name="images",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="rentalcars/",
                verbose_name="Upload Images",
            ),
        ),
    ]