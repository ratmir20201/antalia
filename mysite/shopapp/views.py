from django.shortcuts import render
from django.views.generic import ListView

from .models import Card


class ShopIndexView(ListView):
  template_name = "shopapp/index.html"
  model = Card
  context_object_name = "cards"
