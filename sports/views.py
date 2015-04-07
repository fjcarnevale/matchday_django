from django.shortcuts import render
from django.http import HttpResponse

from .models import League,Team,Match

# Create your views here.

def index(request):
  leagues = League.objects.all()
  context = {'leagues':leagues}
  return render(request, 'sports/index.html', context)
