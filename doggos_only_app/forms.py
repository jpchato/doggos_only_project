from django import forms
from .models import *
from django.forms import ModelForm

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['dog_name', 'dog_size', 'dog_picture']