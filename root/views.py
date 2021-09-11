from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

# Create your views here.

from colors.models import Color, Pigment
from categories.models import Category
from grains.models import Grain

def index(request):
    colors = Color.objects.all()
    categories = Category.objects.all()
    grains = Grain.objects.all()
    context = {'colors': colors, 'categories': categories, 'grains': grains}
    return render(request, 'root/index.html', context)