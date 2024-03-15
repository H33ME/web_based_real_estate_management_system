from django.urls import path

from property.views import PropertyHomePageView, PropertyView,\
    AddNewPropertyView, PropertyAboutView, \
    PropertyTypeView, PropertyAddPropertyTypeView, \
    PropertyEditPropertyTypeView, PropertyEditPropertyView, \
    PropertyDeletePropertyTypeView, PropertyDeletePropertyView, \
    TenantRentPropertyView, TenantPropertyRentedView, \
    TenantsRentedPropertyView, AddPropertyRentPaymentView,\
    PropertyRentPaymentView, EditPropertyRentPaymentTransactionStatusView,\
    PropertyDeletePropertyRentPaymentView, PropertyDeleteTenantView

urlpatterns = [
    path('', PropertyHomePageView.as_view(), name = 'home'),
    path('property/', PropertyView.as_view(), name = 'property'),
    path('add_property/', AddNewPropertyView.as_view(), name = 'add_property'),
    path('about/', PropertyAboutView.as_view(), name = 'about'),
    path('property_types/', PropertyTypeView.as_view(), name = 'property_type'),
    path('property_type/create_property_type/',PropertyAddPropertyTypeView.as_view(), name = 'create_property_type'),
    path('property_type/edit_property_type/<int:property_type_id>/', PropertyEditPropertyTypeView.as_view(), name = 'edit_property_type'),
    path('property/edit_property/<int:property_id>/', PropertyEditPropertyView.as_view(), name = 'edit_property'),
    path('property_type/delete_property_type/<int:property_type_id>/', PropertyDeletePropertyTypeView.as_view(), name = 'delete_property_type'),
    path('property/delete_property/<int:property_id>/', PropertyDeletePropertyView.as_view(), name = 'delete_property'),
    path('property/rent_property/<int:property_id>/', TenantRentPropertyView.as_view(), name = 'rent_property'),
    path('property/property_rented/', TenantPropertyRentedView.as_view(), name = 'property_rented'),
    path('property/property_rented/tenants', TenantsRentedPropertyView.as_view(), name = 'tenants'),
    path('property/property_rented/add_property_rent_payment/<int:property_rented_id>/', AddPropertyRentPaymentView.as_view(), name = 'add_property_rent_payment'),
    path('property/property_rented/property_rent_details', PropertyRentPaymentView.as_view(), name = 'property_rent_details'),
    path('property/property_rented/update_property_rent_payment_transaction_status/<int:rent_payment_id>/', EditPropertyRentPaymentTransactionStatusView.as_view(), name = 'update_property_rent_payment_transaction_status'),
    path('property/property_rented/delete_property_rent_payment/<int:rent_payment_id>/', PropertyDeletePropertyRentPaymentView.as_view(), name = 'delete_property_rent_payment'),
    path('property/property_rented/tenants/delete_tenant/<int:tenant_id>/', PropertyDeleteTenantView.as_view(), name = 'delete_tenant')
]