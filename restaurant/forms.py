from urllib.request import Request
from django.forms import ModelForm
from django import forms
from django.http import request
from .models import Restaurant, Menu


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['user', 'name', 'address']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'id': 'userpk'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['meal', 'ingredients', 'price', 'image']
        widgets = {
            'meal': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
