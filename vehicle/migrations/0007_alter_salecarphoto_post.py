# Generated by Django 3.2.4 on 2021-07-03 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0006_auto_20210704_0046"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salecarphoto",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="vehicle.forsalecar"
            ),
        ),
    ]
