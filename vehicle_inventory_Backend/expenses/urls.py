from django.urls import path
from .views import expenses_home

urlpatterns = [
    path('', expenses_home, name='expenses_home'),
] 