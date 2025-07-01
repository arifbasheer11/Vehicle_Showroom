from django.urls import path
from .views import users_home

urlpatterns = [
    path('', users_home, name='users_home'),
] 