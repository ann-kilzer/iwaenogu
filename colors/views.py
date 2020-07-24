from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Color, Pigment
from categories.models import Category
from grains.models import Grain
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
    categories = set([p.category for p in pigments])
    return render(request, 'colors/color_detail.html', {'color': color, 'pigments': pigments, 'categories': categories})

def categories_subindex(request, color_id):
    color = get_object_or_404(Color, pk=color_id)
    pigments = Pigment.objects.filter(color=color)
    categories = set([p.category for p in pigments])
    return render(request, 'colors/categories_subindex.html', {'color': color, 'categories': categories})

def category_detail(request, color_id, category_code):
    color = get_object_or_404(Color, pk=color_id)
    category = Category.objects.get(pk=category_code)
    pigments = Pigment.objects.filter(color=color)
    grains= set([p.grain for p in pigments])
    return render(request, 'colors/category_detail.html', {'color': color, 'category': category, 'grains': grains})

def grains_subindex(request, color_id, category_code):
    color = get_object_or_404(Color, pk=color_id)
    category = Category.objects.get(pk=category_code)
    pigments = Pigment.objects.filter(color=color)
    grains= set([p.grain for p in pigments])
    return render(request, 'colors/grains_subindex.html', {'color': color, 'category': category, 'grains': grains})

def grain_detail(request, color_id, category_code, grain_id):
    color = get_object_or_404(Color, pk=color_id)
    category = Category.objects.get(pk=category_code)
    grain = Grain.objects.get(pk=grain_id)
    # TODO: get the pigment
    return render(request, 'colors/grain_detail.html', {'color': color, 'category': category, 'grain': grain})
