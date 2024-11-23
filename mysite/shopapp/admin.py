from django.contrib import admin

from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image', 'description', 'price')
    list_filter = ('pk',)
