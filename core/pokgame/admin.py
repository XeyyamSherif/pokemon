from django.contrib import admin
from .models import pokemons


@admin.register(pokemons)
class CourseAdmin(admin.ModelAdmin):
    pass
