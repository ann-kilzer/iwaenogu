from django.urls import path

from . import views

urlpatterns = [
    # ex: /colors/
    path('', views.index, name='index'),
    # ex: /colors/5/
    path('<int:color_id>/', views.color, name='color'),
    # ex: /colors/5/categories/
    path('<int:color_id>/categories/', views.categories_subindex, name='categories_subindex'),
    # ex: /colors/5/categories/3
    path('<int:color_id>/categories/<str:category_code>/', views.category_detail, name='category_detail'),
    # ex: /colors/5/categories/3/grains
    path('<int:color_id>/categories/<str:category_code>/grains', views.category_detail, name='category_detail'),
    # ex: /colors/5/categories/3/grains/5
    path('<int:color_id>/categories/<str:category_code>/grains/<int:grain_id>', views.grain_detail, name='grain_detail'),
]