from django.shortcuts import render
from .forms import *
from .models import Dog
from django.views import generic
from django.views.generic.detail import DetailView
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            plural_dog = Dog.objects.all()
            return render(request, 'doggos_only_app/dog_images.html', {'dog_images' : plural_dog})
    else:
        form = DogForm()
    return render(request, 'doggos_only_app/home.html', {'form' : form})

def display_images(request):
    if request.method == 'GET':
        plural_dog = Dog.objects.all()
        return render(request, 'doggos_only_app/dog_images.html', {'dog_images' : plural_dog})

class DogDetailView(generic.DetailView):
    model = Dog
    def get_context_data(self, *args, **kwargs):
        context = super(DogDetailView, self).get_context_data(*args, **kwargs)
        return context