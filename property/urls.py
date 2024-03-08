from django.urls import path

from property.views import PropertyHomePageView, PropertyView,\
    AddNewPropertyView, PropertyAboutView, \
    PropertyTypeView, PropertyAddPropertyTypeView, \
    PropertyEditPropertyTypeView, PropertyEditPropertyView, \
    PropertyDeletePropertyTypeView, PropertyDeletePropertyView

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
    path('property/delete_property/<int:property_id>/', PropertyDeletePropertyView.as_view(), name = 'delete_property')
]