from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Color, Pigment
# Create your views here.

def index(request):
    colors = Color.objects.order_by('hex_code')
    context = {
        'colors': colors,
    }
    return render(request, 'colors/index.html', context)

def color(request, color_id):
    color = get_object_or_404(Color, pk=color_id)
    pigments = Pigment.objects.filter(color=color)
    return render(request, 'colors/detail.html', {'color': color, 'pigments': pigments})

def pigment(request, color_id, pigment_id):
    response = "You're looking at the results of color %s."
    return HttpResponse(response % color_id)

def vote(request, color_id):
    return HttpResponse("You're voting on color %s." % color_id)
