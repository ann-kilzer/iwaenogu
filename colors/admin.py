from django.contrib import admin

from .models import ColorFamily, Pigment, Color

admin.site.register(Pigment)
admin.site.register(Color)
admin.site.register(ColorFamily)