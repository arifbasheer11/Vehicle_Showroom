from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

def employees_home(request):
    return HttpResponse("Welcome to the Employees Home Page!")

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
