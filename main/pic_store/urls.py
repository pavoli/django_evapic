from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pictures/', views.pictures, name='pictures'),
    path('about/', views.pictures, name='about'),
]