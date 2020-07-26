from django.urls import path

from . import views

urlpatterns = [
    # /categories/
    path('', views.index, name='index'),
    path('<str:category_code>/', views.category, name='category'),
]