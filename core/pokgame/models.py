from django.db import models
from django.contrib.auth.models import User


class pokemons(models.Model):
    gamer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.TextField()
    url = models.URLField(max_length=250)
