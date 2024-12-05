from django.urls import path
from .views import ShopIndexView, messages_view

app_name = "shopapp"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("api/messages/", messages_view, name="messages"),
    # path('api/messages/', get_messages, name='get_messages'),
    # path('api/messages/', post_message, name='post_message'),
]
