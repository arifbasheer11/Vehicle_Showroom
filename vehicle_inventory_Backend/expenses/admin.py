from django.contrib import admin
from .models import Expense, ExpenseCategory, FuelExpense

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class FuelExpenseInline(admin.StackedInline):
    model = FuelExpense
    extra = 0
    fields = ('fuel_type', 'liters', 'price_per_liter', 'mileage_at_fuel', 'gas_station')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'category', 'amount', 'expense_date', 'payment_method', 'is_reimbursed')
    list_filter = ('category', 'payment_method', 'expense_date', 'is_reimbursed')
    search_fields = ('vehicle__license_plate', 'vehicle__make', 'vehicle__model', 'description', 'vendor')
    list_editable = ('is_reimbursed',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [FuelExpenseInline]
    
    fieldsets = (
        ('Expense Details', {
            'fields': ('vehicle', 'category', 'amount', 'description')
        }),
        ('Payment Information', {
            'fields': ('payment_method', 'receipt_number', 'expense_date')
        }),
        ('Vendor & Location', {
            'fields': ('vendor', 'location')
        }),
        ('User Information', {
            'fields': ('created_by', 'is_reimbursed')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(FuelExpense)
class FuelExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense', 'fuel_type', 'liters', 'price_per_liter', 'gas_station')
    list_filter = ('fuel_type', 'gas_station')
    search_fields = ('expense__vehicle__license_plate', 'gas_station')
