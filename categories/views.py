from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Category
# Create your views here.

def index(request):
    categories = Category.objects.order_by('code')
    return render(request, 'categories/index.html', {'categories': categories})

def category(request, category_code):
    category = get_object_or_404(Category, pk=category_code)
    return render(request, 'categories/detail.html', {'category': category})