from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('dog_images', views.display_images, name='dog_images'),
    path('<int:pk>', views.DogDetailView.as_view(), name='dog_detail')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)