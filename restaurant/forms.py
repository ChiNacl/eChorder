from django.forms import ModelForm
from .models import Restaurant, Menu


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
