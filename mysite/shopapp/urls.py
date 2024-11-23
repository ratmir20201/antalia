from django.urls import path
from .views import ShopIndexView

app_name = "shopapp"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
]
