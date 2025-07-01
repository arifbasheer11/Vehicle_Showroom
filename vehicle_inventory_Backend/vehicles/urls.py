from django.urls import path
from .views import vehicles_home, add_vehicle

urlpatterns = [
    path('', vehicles_home, name='vehicles_home'),
    path('add/', add_vehicle, name='add_vehicle'),
] 