# Generated by Django 3.2.4 on 2021-07-05 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0007_alter_salecarphoto_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rentcarphoto",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="vehicle.rentalcar"
            ),
        ),
    ]