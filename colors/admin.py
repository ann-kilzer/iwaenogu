from django.contrib import admin

from .models import Pigment, Color, PigmentType

admin.site.register(Pigment)
admin.site.register(Color)
admin.site.register(PigmentType)