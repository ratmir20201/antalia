from django.db import models
from django.utils.timezone import now


class Card(models.Model):
    image = models.ImageField(null=False, upload_to="cards/")
    description = models.TextField(null=False)
    price = models.IntegerField(null=False)


class Message(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.username}: {self.content[:20]}"
