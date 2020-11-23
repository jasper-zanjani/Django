from django.contrib import admin
from .models import Starship, StarshipClass

# Register your models here.
admin.site.register(StarshipClass)
admin.site.register(Starship)