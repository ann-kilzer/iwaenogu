from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Grain
# Create your views here.

def index(request):
    grains = Grain.objects.order_by('id')
    return render(request, 'grains/index.html', {'grains': grains})

def grain(request, grain_id):
    grain = get_object_or_404(Grain, pk=grain_id)
    return render(request, 'grains/detail.html', {'grain': grain})