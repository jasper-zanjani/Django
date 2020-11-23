from django.shortcuts import render
from .models import Starship

def index(request):
  ships = Starship.objects.all()
  context = {'ships': ships}
  return render(request, 'dist/index.html', context)