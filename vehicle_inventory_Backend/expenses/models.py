from django.db import models
from users.models import User
from vehicles.models import Vehicle

class ExpenseCategory(models.Model):
    """Expense categories"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'expense_categories'
        verbose_name_plural = 'Expense Categories'

class Expense(models.Model):
    """Vehicle expense model"""
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('check', 'Check'),
    ]
    
    # Basic Information
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    
    # Payment Details
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    receipt_number = models.CharField(max_length=100, blank=True)
    
    # Dates
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # User tracking
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Additional fields
    vendor = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    is_reimbursed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.vehicle} - {self.category} - ${self.amount} on {self.expense_date}"
    
    class Meta:
        db_table = 'expenses'

class FuelExpense(models.Model):
    """Specific fuel expense tracking"""
    expense = models.OneToOneField(Expense, on_delete=models.CASCADE, related_name='fuel_details')
    fuel_type = models.CharField(max_length=20, choices=Vehicle.FUEL_TYPES)
    liters = models.DecimalField(max_digits=8, decimal_places=2)
    price_per_liter = models.DecimalField(max_digits=6, decimal_places=2)
    mileage_at_fuel = models.IntegerField()
    gas_station = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.expense.vehicle} - {self.liters}L {self.fuel_type} at {self.gas_station}"
    
    class Meta:
        db_table = 'fuel_expenses'
