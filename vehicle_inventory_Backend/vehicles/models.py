from django.db import models
from users.models import User

class VehicleType(models.Model):
    """Vehicle type/category"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'vehicle_types'

class Vehicle(models.Model):
    """Vehicle model"""
    FUEL_TYPES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
        ('lpg', 'LPG'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('maintenance', 'Under Maintenance'),
        ('retired', 'Retired'),
        ('sold', 'Sold'),
    ]
    
    # Basic Information
    license_plate = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, unique=True, blank=True, null=True)
    
    # Technical Details
    engine_size = models.CharField(max_length=50, blank=True)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPES)
    transmission = models.CharField(max_length=50, blank=True)
    mileage = models.IntegerField(default=0)
    
    # Ownership & Status
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    assigned_driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_vehicles')
    
    # Financial
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Dates
    purchase_date = models.DateField(blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    insurance_expiry = models.DateField(blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.make} {self.model} - {self.license_plate}"
    
    class Meta:
        db_table = 'vehicles'

class VehicleMaintenance(models.Model):
    """Vehicle maintenance records"""
    MAINTENANCE_TYPES = [
        ('routine', 'Routine Service'),
        ('repair', 'Repair'),
        ('inspection', 'Inspection'),
        ('emergency', 'Emergency'),
    ]
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenance_records')
    maintenance_type = models.CharField(max_length=20, choices=MAINTENANCE_TYPES)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    service_provider = models.CharField(max_length=200)
    service_date = models.DateField()
    next_service_date = models.DateField(blank=True, null=True)
    mileage_at_service = models.IntegerField()
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.vehicle} - {self.maintenance_type} on {self.service_date}"
    
    class Meta:
        db_table = 'vehicle_maintenance'
