from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Color
# Create your views here.

def index(request):
    colors = Color.objects.order_by('hex_code')
    template = loader.get_template('colors/index.html')
    context = {
        'colors': colors,
    }
    return HttpResponse(template.render(context, request))

def color(request, color_id):
    return HttpResponse("You're looking at color %s." % color_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
