from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import AssetModel, User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# view for all assets available can have specific type drop down to pick type to list
# put in an add button to add new asset when on all select
class AssetView(ListView):
    model = AssetModel
    template_name = "assetmgt/all_assets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


# view for all users available
class UserView(ListView):
    model = User
    template_name = "assetmgt/all_users.html"


# view for specific asset and accessories attached to it and user allotted
# give rud functionality here
# assign user button
class AssetDetail(DetailView):
    model = AssetModel
    template_name = "assetmgt/asset_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = AssetModel._meta.fields
        context["fields"] = fields
        print(context)
        return context


class AssetCreateView(CreateView):
    model = AssetModel
    fields = "__all__"
    template_name = "assetmgt/addasset.html"


class AssetUpdateView(UpdateView):
    model = AssetModel
    fields = "__all__"
    template_name = "assetmgt/updateasset.html"


class AssetDeleteView(DeleteView):
    model = AssetModel
    success_url = reverse_lazy("assetmgt:assetlist")
    template_name = "assetmgt/deleteasset.html"
