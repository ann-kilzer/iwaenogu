from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:color_id>/', views.color, name='color'),
    # ex: /polls/5/results/
    path('<int:color_id>/pigments/', views.pigment, name='pigments'),
    # ex: /polls/5/vote/
    path('<int:color_id>/vote/', views.vote, name='vote'),
]