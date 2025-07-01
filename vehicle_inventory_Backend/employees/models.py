from django.db import models
from users.models import User

class Department(models.Model):
    """Company departments"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'departments'

class Employee(models.Model):
    """Employee model"""
    EMPLOYMENT_STATUS = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('terminated', 'Terminated'),
        ('on_leave', 'On Leave'),
    ]
    
    DRIVER_LICENSE_TYPES = [
        ('class_a', 'Class A'),
        ('class_b', 'Class B'),
        ('class_c', 'Class C'),
        ('class_d', 'Class D'),
        ('motorcycle', 'Motorcycle'),
    ]
    
    # Basic Information
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS, default='active')
    
    # Employment Details
    hire_date = models.DateField()
    termination_date = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Driver Information
    is_driver = models.BooleanField(default=False)
    driver_license_number = models.CharField(max_length=50, blank=True)
    driver_license_type = models.CharField(max_length=20, choices=DRIVER_LICENSE_TYPES, blank=True)
    driver_license_expiry = models.DateField(blank=True, null=True)
    
    # Contact Information
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"
    
    class Meta:
        db_table = 'employees'

class DriverSchedule(models.Model):
    """Driver work schedules"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.employee} - {self.date} ({self.start_time} - {self.end_time})"
    
    class Meta:
        db_table = 'driver_schedules'
