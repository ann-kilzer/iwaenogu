from django.urls import path

from . import views

urlpatterns = [
    # ex: /colors/
    path('', views.index, name='index'),
    # ex: /colors/5/
    path('<int:color_id>/', views.color, name='color'),
    # ex: /colors/5/pigments/
    path('<int:color_id>/pigments/', views.pigments_subindex, name='pigments_subindex'),
    # ex: /colors/5/pigments/3
    path('<int:color_id>/pigments/<int:pigment_id>/', views.color_pigment, name='color_pigment'),
]