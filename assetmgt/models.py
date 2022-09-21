from django.db import models
from qux.models import CoreModel
from django.urls import reverse
from django.forms import ModelForm
from django.contrib.auth.models import User

ASSET_TYPE = [
    ("CPU", "CPU"),
    ("Keyboard", "Keyboard"),
    ("Mouse", "Mouse"),
    ("Monitor", "Monitor"),
]


class Users(User):
    emp_id = models.CharField(max_length=10, verbose_name="Employee ID")
    emp_name = models.CharField(max_length=50, verbose_name="Name")

    def __str__(self):
        return self.emp_name


class AssetModel(CoreModel):
    model_id = models.CharField(max_length=20, verbose_name="Model ID")
    brand_name = models.CharField(max_length=15, verbose_name="Brand")
    type_of_asset = models.CharField(
        blank=False, choices=ASSET_TYPE, max_length=30, verbose_name="Type"
    )
    date_procured = models.DateField(verbose_name="Date Procured")
    price = models.FloatField(verbose_name="Price")
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        default=None,
        blank=True,
        verbose_name="User",
    )
    date_allotted = models.DateField(
        null=True, default=None, verbose_name="Date Allotted"
    )

    # def __str__(self):
    #     return str(id) + self.type_of_asset

    def get_absolute_url(self):
        return reverse("assetmgt:assetdetail", kwargs={"pk": self.pk})


class Accessories(CoreModel):
    model_id = models.CharField(max_length=30, verbose_name="Model ID")
    accessory_type = models.CharField(max_length=20, verbose_name="Type")
    asset = models.ForeignKey(
        AssetModel, on_delete=models.CASCADE, verbose_name="Of Asset"
    )

    # def __str__(self):
    #     return str(id) + self.accessory_type


# class AssetForm(ModelForm):
#     class Meta:
#         model = AssetModel
#         fields = "__all__"
