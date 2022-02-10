from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/', views.RestaurantView.as_view(), name='restaurants'),
    path('restaurant/<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant'),
    path('createrestaurant/', views.CreateRestaurant.as_view(), name='create_restaurant'),
]