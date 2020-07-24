from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Color, Pigment
from categories.models import Category
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
    return render(request, 'colors/color_detail.html', {'color': color, 'pigments': pigments})

def categories_subindex(request, color_id):
    color = get_object_or_404(Color, pk=color_id)
    pigments = Pigment.objects.filter(color=color)
    categories = set([p.category for p in pigments])
    return render(request, 'colors/categories_subindex.html', {'color': color, 'categories': categories})

def category_detail(request, color_id, category_code):
    color = get_object_or_404(Color, pk=color_id)
    category = Category.objects.get(pk=category_code)
    return render(request, 'colors/category_detail.html', {'color': color, 'category': category})

def grains_subindex(request, color_id, pigment_id):
    color = get_object_or_404(Color, pk=color_id)
    pigment = Pigment.objects.get(color=color, pk=pigment_id)
    return render(request, 'colors/pigment_detail.html', {'color': color, 'pigment': pigment})

def color_pigment_grain(request, color_id, pigment_id, grain_id):
    return HttpResponse("You're looking at color %s %s %s" % (color_id, pigment_id, grain_id))
