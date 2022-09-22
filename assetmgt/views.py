from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import AssetModel, Accessories
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User

# view for all assets available can have specific type drop down to pick type to list
class AssetView(ListView):
    model = AssetModel
    template_name = "assetmgt/all_assets.html"

    def get_queryset(self):
        type = self.request.GET.get("type", None)
        if type == None:
            queryset = super().get_queryset()
        else:
            queryset = AssetModel.objects.filter(type_of_asset=type)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# view for all users available
class UserView(ListView):
    model = User
    template_name = "assetmgt/all_users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


# view for specific asset and accessories attached to it and user allotted
# give rud functionality here
# assign user button
class AssetDetail(DetailView):
    model = AssetModel
    template_name = "assetmgt/asset_detail.html"
    # handle selected from the list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = AssetModel._meta.fields
        context["fields"] = fields
        return context


class AssetCreateView(CreateView):
    model = AssetModel
    fields = "__all__"
    template_name = "assetmgt/addasset.html"


class AssetUpdateView(UpdateView):
    model = AssetModel
    fields = "__all__"
    template_name = "assetmgt/updateasset.html"
    # before update check if user is super user if not dont update send msg


class AssetDeleteView(DeleteView):
    model = AssetModel
    success_url = reverse_lazy("assetmgt:assetlist")
    template_name = "assetmgt/deleteasset.html"
    # before delete check if user is super user if not dont delete send msg


# Accessories Views


class AccessoriesView(ListView):
    model = Accessories
    template_name = "assetmgt/all_accessories.html"


class AccessoryDetail(DetailView):
    model = Accessories
    template_name = "assetmgt/accessory_detail.html"
    # handle selected from the list


class AccessoryCreateView(CreateView):
    model = Accessories
    fields = "__all__"
    template_name = "assetmgt/addaccessory.html"


class AccessoryUpdateView(UpdateView):
    model = Accessories
    fields = "__all__"
    template_name = "assetmgt/updateaccessory.html"
    # before update check if user is super user if not dont update send msg


class AccessoryDeleteView(DeleteView):
    model = Accessories
    success_url = reverse_lazy("assetmgt:accessorylist")
    template_name = "assetmgt/deleteaccessory.html"
    # before delete check if user is super user if not dont delete send msg
