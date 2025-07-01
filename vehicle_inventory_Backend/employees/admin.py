from django.contrib import admin
from .models import Employee, Department, DriverSchedule

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class DriverScheduleInline(admin.TabularInline):
    model = DriverSchedule
    extra = 0
    fields = ('date', 'start_time', 'end_time', 'is_available')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'department', 'position', 'employment_status', 'is_driver')
    list_filter = ('employment_status', 'department', 'is_driver', 'hire_date')
    search_fields = ('employee_id', 'user__username', 'user__first_name', 'user__last_name', 'position')
    list_editable = ('employment_status', 'is_driver')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [DriverScheduleInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'employee_id', 'department', 'position', 'employment_status')
        }),
        ('Employment Details', {
            'fields': ('hire_date', 'termination_date', 'salary')
        }),
        ('Driver Information', {
            'fields': ('is_driver', 'driver_license_number', 'driver_license_type', 'driver_license_expiry')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relationship')
        }),
        ('Metadata', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(DriverSchedule)
class DriverScheduleAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'start_time', 'end_time', 'is_available')
    list_filter = ('date', 'is_available')
    search_fields = ('employee__user__username', 'employee__user__first_name', 'employee__user__last_name')
    list_editable = ('is_available',)
    readonly_fields = ('created_at', 'updated_at')
