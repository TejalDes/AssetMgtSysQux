# Generated by Django 4.1.1 on 2022-09-19 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("assetmgt", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="user",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="assetmgt.user",
            ),
        ),
    ]
