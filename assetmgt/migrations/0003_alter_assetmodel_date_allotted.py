# Generated by Django 4.1.1 on 2022-09-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assetmgt", "0002_alter_assetmodel_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="date_allotted",
            field=models.DateField(default=None, null=True),
        ),
    ]