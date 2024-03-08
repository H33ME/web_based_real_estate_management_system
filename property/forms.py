from django import forms
from property.models import Property, PropertyType

class AddNewPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('name', 'property_type', 'description', 'location', 'bathrooms','number_available', 'bedrooms', 'price')

    def __init__(self, *args, **kwargs):
        super(AddNewPropertyForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Add device name'
        self.fields['property_type'].widget.attrs['placeholder'] = 'Choose property type'
        self.fields['location'].widget.attrs['placeholder'] = 'Enter location'
        self.fields['bathrooms'].widget.attrs['placeholder'] = 'Enter number of bathrooms'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter device description'
        self.fields['bedrooms'].widget.attrs['placeholder'] = 'Enter bedrooms available'
        self.fields['number_available'].widget.attrs['placeholder'] = 'Enter number of property available'
        self.fields['price'].widget.attrs['placeholder'] = 'Select house price'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['property_type'].widget.attrs['class'] = 'form-control select2_se'

class EditPropertyTypeForm(forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = ('name', )
        def __init__(self, *args, **kwargs):
            super(EditPropertyTypeForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs['placeholder'] = 'Edit name'

class EditPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('name', 'property_type', 'description', 'location', 'bathrooms','number_available', 'bedrooms', 'price')
    def __init__(self, *args, **kwargs):
        super(EditPropertyForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'edit device name'
        self.fields['property_type'].widget.attrs['placeholder'] = 'Choose property type'
        self.fields['location'].widget.attrs['placeholder'] = 'edit location'
        self.fields['bathrooms'].widget.attrs['placeholder'] = 'edit number of bathrooms'
        self.fields['description'].widget.attrs['placeholder'] = 'edit device description'
        self.fields['bedrooms'].widget.attrs['placeholder'] = 'edit bedrooms available'
        self.fields['number_available'].widget.attrs['placeholder'] = 'edit number of property available'
        self.fields['price'].widget.attrs['placeholder'] = 'Select house price'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['property_type'].widget.attrs['class'] = 'form-control select2_se'