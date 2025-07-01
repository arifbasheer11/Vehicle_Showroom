from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def users_home(request):
    return HttpResponse("Welcome to the Users Home Page!")
