from pokgame.models import pokemons
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
import requests
import json
from .serializer import PokemonSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'registration.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("invalid user")
    return render(request, 'login.html')


def logout_from_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def addPokemon(request, name):
    new_pokemon = pokemons(
        name=name,
        gamer=request.user
    )
    new_pokemon.save()
    return redirect('cabinet')


@login_required(login_url='/login/')
def home(request):
    pokemons = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10')
    all_pokes = json.loads(pokemons.text)
    return render(request, "home.html", {'pokemons': all_pokes['results']})


def cabinet(request):
    pokemons_of_user = pokemons.objects.filter(gamer=request.user)
    return render(request, "cabinet.html", {'pokemons_of_user':  pokemons_of_user})


@ api_view(["GET"])
def PokemonList(request):
    pkemons_all = User.objects.all()
    ser_poke = UserSerializer(pkemons_all, many=True)
    return Response(ser_poke.data)
