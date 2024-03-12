from django.contrib import admin
from tenants.models import Tenant
# Register your models here.
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    """
    Admin View for Tenant
    """
    list_display = ['first_name','last_name', 'email', 'phone_number', 'occupation', 'emergency_contact', ]
    list_filter = ['first_name','last_name', 'email', 'phone_number', 'occupation', 'emergency_contact', ]