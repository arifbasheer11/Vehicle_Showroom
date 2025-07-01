from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def expenses_home(request):
    return HttpResponse("Welcome to the Expenses Home Page!")
