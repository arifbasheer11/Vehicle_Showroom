from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'license_plate', 'make', 'model', 'year', 'color', 'vin',
            'engine_size', 'fuel_type', 'transmission', 'mileage',
            'vehicle_type', 'status', 'assigned_driver',
            'purchase_price', 'current_value',
            'purchase_date', 'registration_date', 'insurance_expiry',
            'notes'
        ]
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'insurance_expiry': forms.DateInput(attrs={'type': 'date'}),
        } 