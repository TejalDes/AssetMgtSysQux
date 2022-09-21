# Generated by Django 4.1.1 on 2022-09-19 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                    "dtm_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="DTM Created"),
                ),
                (
                    "dtm_updated",
                    models.DateTimeField(auto_now=True, verbose_name="DTM Updated"),
                ),
                ("emp_id", models.CharField(max_length=10)),
                ("emp_name", models.CharField(max_length=50, verbose_name="name")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AssetModel",
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
                    "dtm_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="DTM Created"),
                ),
                (
                    "dtm_updated",
                    models.DateTimeField(auto_now=True, verbose_name="DTM Updated"),
                ),
                ("model_id", models.CharField(max_length=20)),
                ("brand_name", models.CharField(max_length=15)),
                (
                    "type_of_asset",
                    models.CharField(
                        choices=[
                            ("CPU", "Cpu"),
                            ("Keyboard", "Keyboard"),
                            ("Mouse", "Mouse"),
                            ("Monitor", "Monitor"),
                        ],
                        max_length=30,
                    ),
                ),
                ("date_procured", models.DateField()),
                ("price", models.FloatField()),
                ("date_allotted", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        default=0,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="assetmgt.user",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Accessories",
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
                    "dtm_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="DTM Created"),
                ),
                (
                    "dtm_updated",
                    models.DateTimeField(auto_now=True, verbose_name="DTM Updated"),
                ),
                ("model_id", models.CharField(max_length=30)),
                ("accessory_type", models.CharField(max_length=20)),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assetmgt.assetmodel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]