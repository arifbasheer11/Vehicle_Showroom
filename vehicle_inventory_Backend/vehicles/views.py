from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VehicleForm

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def vehicles_home(request):
    return HttpResponse("Welcome to the Vehicles Home Page!")

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicles_home')
    else:
        form = VehicleForm()
    return render(request, 'add_vehicle.html', {'form': form})
