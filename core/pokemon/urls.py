"""pokemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pokgame import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', views.registration),
    path('login/', views.login_view),
    path('home/', views.home, name='home'),
    path('addPoke/<str:name>/', views.addPokemon),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('api/pokemons/', views.PokemonList),
    path('logout/', views.logout_from_user, name='login_view')
]
