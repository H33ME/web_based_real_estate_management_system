from django.contrib import admin
from payments.models import RentPayment
# Register your models here.
@admin.register(RentPayment)
class RentPaymentAdmin(admin.ModelAdmin):
    """
    Admin View for RentPayment
    """
    list_display = ['rent_property','amount_paid','payment_date','payment_method', 'payment_reference','transaction_status']
    list_filter = ['rent_property','amount_paid','payment_date','payment_method', 'payment_reference','transaction_status']
