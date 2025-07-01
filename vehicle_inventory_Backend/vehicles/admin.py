from django.contrib import admin
from .models import Vehicle, VehicleType, VehicleMaintenance

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'make', 'model', 'year', 'status', 'assigned_driver', 'vehicle_type')
    list_filter = ('status', 'fuel_type', 'vehicle_type', 'year')
    search_fields = ('license_plate', 'make', 'model', 'vin')
    list_editable = ('status', 'assigned_driver')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('license_plate', 'make', 'model', 'year', 'color', 'vin')
        }),
        ('Technical Details', {
            'fields': ('engine_size', 'fuel_type', 'transmission', 'mileage')
        }),
        ('Ownership & Status', {
            'fields': ('vehicle_type', 'status', 'assigned_driver')
        }),
        ('Financial', {
            'fields': ('purchase_price', 'current_value')
        }),
        ('Important Dates', {
            'fields': ('purchase_date', 'registration_date', 'insurance_expiry')
        }),
        ('Metadata', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(VehicleMaintenance)
class VehicleMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'maintenance_type', 'service_date', 'cost', 'service_provider')
    list_filter = ('maintenance_type', 'service_date', 'service_provider')
    search_fields = ('vehicle__license_plate', 'vehicle__make', 'vehicle__model', 'description')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Maintenance Details', {
            'fields': ('vehicle', 'maintenance_type', 'description', 'cost')
        }),
        ('Service Information', {
            'fields': ('service_provider', 'service_date', 'next_service_date', 'mileage_at_service')
        }),
        ('Performed By', {
            'fields': ('performed_by',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
