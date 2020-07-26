from django.urls import path

from . import views

urlpatterns = [
    # /grains/
    path('', views.index, name='index'),
    path('<int:grain_id>/', views.grain, name='grain'),
]