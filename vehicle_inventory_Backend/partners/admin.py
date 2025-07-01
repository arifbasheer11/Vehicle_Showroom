from django.contrib import admin
from .models import Partner, ServiceContract

class ServiceContractInline(admin.TabularInline):
    model = ServiceContract
    extra = 0
    fields = ('contract_number', 'service_type', 'start_date', 'end_date', 'status', 'total_value')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'partner_type', 'status', 'contact_person', 'phone')
    list_filter = ('partner_type', 'status')
    search_fields = ('name', 'contact_person', 'email', 'phone')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ServiceContractInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'partner_type', 'status')
        }),
        ('Contact Information', {
            'fields': ('contact_person', 'email', 'phone', 'address', 'website')
        }),
        ('Business Details', {
            'fields': ('tax_id', 'registration_number')
        }),
        ('Financial', {
            'fields': ('credit_limit', 'payment_terms')
        }),
        ('Metadata', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ServiceContract)
class ServiceContractAdmin(admin.ModelAdmin):
    list_display = ('contract_number', 'partner', 'service_type', 'start_date', 'end_date', 'status', 'total_value')
    list_filter = ('status', 'start_date', 'end_date', 'service_type')
    search_fields = ('contract_number', 'partner__name', 'service_type', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Contract Information', {
            'fields': ('partner', 'contract_number', 'service_type', 'description')
        }),
        ('Contract Terms', {
            'fields': ('start_date', 'end_date', 'status')
        }),
        ('Financial Terms', {
            'fields': ('total_value', 'payment_schedule')
        }),
        ('Contact Information', {
            'fields': ('contact_person', 'contact_phone', 'contact_email')
        }),
        ('Metadata', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
