import pytest
from django.contrib.auth.models import User
from pokgame.models import pokemons


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test', 'example@tes.com', 'password')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_add_pokemon():
    gamer = User(username='Xeyyam')
    gamer.save()
    pokemons.objects.create(name='test', gamer=gamer)
    assert pokemons.objects.count() == 1
