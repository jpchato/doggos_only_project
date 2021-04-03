from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dog_images', views.display_images, name='dog_images')
    ]