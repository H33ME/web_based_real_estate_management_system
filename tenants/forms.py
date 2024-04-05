from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tenants.models import RentProperty, Tenant

class CreateNewUserAsTenantForm(UserCreationForm):
    username = forms.EmailField(required=True)
    first_name=forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    occupation = forms.CharField(required=True)
    identification_number = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    emergency_contact = forms.CharField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email',  'password1', 'password2', 'occupation', 'identification_number', 'phone_number', 'emergency_contact')
        def __init__(self, *args, **kwargs):
            super(CreateNewUserAsTenantForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'create last name'
            self.fields['username'].widget.attrs['placeholder'] = 'create username'
            self.fields['occupation'].widget.attrs['placeholder'] = 'select occupation'
            self.fields['identification_number'].widget.attrs['placeholder'] = 'Enter identification number'
            self.fields['emergency_contact'].widget.attrs['placeholder'] = 'Enter emergency contact'

            self.fields['email'].widget.attrs['placeholder'] = 'create email'
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class EditTenantProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    class Meta:
        model = Tenant
        fields = ('first_name','last_name', 'email', 'occupation', 'identification_number', 'phone_number', 'emergency_contact')
        def __init__(self, *args, **kwargs):
            super(EditTenantProfileForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'edit last name'
            self.fields['email'].widget.attrs['placeholder'] = 'edit email'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class RentPropertyForm(forms.ModelForm):
    class Meta:
        model = RentProperty
        fields = ('property', 'move_in_date', 'lease_start_date', 'lease_end_date', 'rent_amount', 'security_deposit', 'additional_notes', 'payment_frequency', 'room_number')

    def __init__(self, *args, **kwargs):
        super(RentPropertyForm, self).__init__(*args, **kwargs)
        # Customize form field widgets or add additional validation if needed
        self.fields['move_in_date'].widget.attrs['class'] = 'datepicker'
        self.fields['lease_start_date'].widget.attrs['class'] = 'datepicker'
        self.fields['lease_end_date'].widget.attrs['class'] = 'datepicker'