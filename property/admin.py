from django.contrib import admin
from property.models import Property, PropertyType
# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """
    Admin View for Property
    """
    list_display = ['property_type','name', 'description', 'price', 'bedrooms', 'bathrooms', 'location', 'created_at', 'updated_at']
    list_filter = ['property_type','name', 'description', 'price', 'bedrooms', 'bathrooms', 'location', 'created_at', 'updated_at']

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    """
    Admin View for Property Type
    """
    list_display= ['name']
    list_filter = ['name']