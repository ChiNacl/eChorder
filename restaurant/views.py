from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RestaurantForm
from .models import Restaurant, Menu
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
    return render(request, 'restaurant/home.html')


class RestaurantView(ListView):
    model = Restaurant
    template_name = 'restaurant/restaurants.html'
    context_object_name = 'restaurants'


class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant/restaurant.html'
    context_object_name = 'restaurant'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['menu'] = self.object.menu.all()
            return context
        except Menu.DoesNotExist:
            return context
            # print(self.object.pk)
        
        # context['menu'] = Menu.objects.filter(restaurant=self.object)


class CreateRestaurant(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    
