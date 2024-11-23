from django.db import models


class Card(models.Model):
    image = models.ImageField(null=False)
    description = models.TextField(null=False)
    price = models.IntegerField(null=False)
