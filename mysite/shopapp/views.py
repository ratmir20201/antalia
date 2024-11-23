from django.shortcuts import render
from django.views.generic import ListView

from .models import Card


class ShopIndexView(ListView):
  model = Card
  template_name = "shopapp/index.html"
