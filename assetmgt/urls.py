from django.urls import path
from assetmgt.views import *
from assetmgt.views import AssetDetail, AssetView, UserView

app_name = "assetmgt"
urlpatterns = [
    path("assets/", AssetView.as_view(), name="assetlist"),
    path("users/", UserView.as_view(), name="userlist"),
    path("<pk>/", AssetDetail.as_view(), name="assetdetail"),
    path("assets/add/", AssetCreateView.as_view(), name="add"),
    path("assets/<int:pk>/", AssetUpdateView.as_view(), name="update"),
    path("assets/<int:pk>/delete/", AssetDeleteView.as_view(), name="delete"),
]
