from django.urls import path
from .views import partners_home

urlpatterns = [
    path('', partners_home, name='partners_home'),
] 