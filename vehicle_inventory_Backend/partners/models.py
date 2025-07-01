from django.db import models

# Create your models here.

class Partner(models.Model):
    """Business partners/vendors"""
    PARTNER_TYPES = [
        ('service_provider', 'Service Provider'),
        ('supplier', 'Supplier'),
        ('vendor', 'Vendor'),
        ('contractor', 'Contractor'),
        ('insurance', 'Insurance Company'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]
    
    # Basic Information
    name = models.CharField(max_length=200)
    partner_type = models.CharField(max_length=20, choices=PARTNER_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    
    # Contact Information
    contact_person = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    website = models.URLField(blank=True)
    
    # Business Details
    tax_id = models.CharField(max_length=50, blank=True)
    registration_number = models.CharField(max_length=50, blank=True)
    
    # Financial
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_terms = models.CharField(max_length=100, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_partner_type_display()}"
    
    class Meta:
        db_table = 'partners'

class ServiceContract(models.Model):
    """Service contracts with partners"""
    CONTRACT_STATUS = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('terminated', 'Terminated'),
        ('pending', 'Pending'),
    ]
    
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='contracts')
    contract_number = models.CharField(max_length=50, unique=True)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    
    # Contract Terms
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=CONTRACT_STATUS, default='pending')
    
    # Financial Terms
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    payment_schedule = models.CharField(max_length=100, blank=True)
    
    # Contact Information
    contact_person = models.CharField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=15, blank=True)
    contact_email = models.EmailField(blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.contract_number} - {self.partner.name}"
    
    class Meta:
        db_table = 'service_contracts'
