from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("restaurant", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Menu(models.Model):
    meal = models.CharField(max_length=255)
    ingredients = models.TextField(default='none')
    price = models.IntegerField()
    restaurant = models.OneToOneField(
        Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="image_uploads/", default="image_uploads/rice-40282_1280.png")

    def __str__(self):
        return self.meal