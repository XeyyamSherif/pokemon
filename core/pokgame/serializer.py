from django.db import models
from rest_framework import fields, serializers
from .models import pokemons
from django.contrib.auth.models import User


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = pokemons
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):
    user_poke = PokemonSerializer(
        source="pokemons_set", read_only=True, many=True)

    class Meta:
        model = User
        fields = ('username', 'user_poke')
