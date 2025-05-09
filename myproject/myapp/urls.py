from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('math/', views.math, name='math'),
    path('comp/', views.comp, name='comp'),
]