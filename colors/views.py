from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Color, ColorFamily, Pigment
from categories.models import Category
from grains.models import Grain
# Create your views here.

def index(request):
    colors = Color.objects.order_by('hex_color')
    color_families = ColorFamily.objects.order_by('order')
    context = {
        'colors': colors,
        'color_families': color_families,
    }
    return render(request, 'colors/index.html', context)

def color(request, color_id):
    color = get_object_or_404(Color, pk=color_id)
    pigments = Pigment.objects.filter(color=color)
    categories = set([p.category for p in pigments])
    return render(request, 'colors/color_detail.html', {'color': color, 'pigments': pigments, 'categories': categories})

def category_detail(request, color_id, category_code):
    color = get_object_or_404(Color, pk=color_id)
    category = Category.objects.get(pk=category_code)
    pigments = Pigment.objects.filter(color=color, category=category).order_by('grain')
    grains= set([p.grain for p in pigments])
    return render(request, 'colors/category_detail.html', {'color': color, 'category': category, 'grains': grains, 'pigments': pigments})

def grain_detail(request, color_id, category_code, grain_id):
    color = get_object_or_404(Color, pk=color_id)
    category = Category.objects.get(pk=category_code)
    grain = Grain.objects.get(pk=grain_id)
    # TODO: get the pigment
    pigment = get_object_or_404(Pigment, color=color, grain=grain, category=category)
    return render(request, 'colors/grain_detail.html', {'color': color, 'category': category, 'grain': grain, 'pigment': pigment})
