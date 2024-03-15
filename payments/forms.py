from django import forms
from payments.models import RentPayment
class CreatePropertyRentedPaymentForm(forms.ModelForm):
    class Meta:
        model = RentPayment
        fields = ('rent_property','amount_paid','payment_method',)
        def __init__(self, *args, **kwargs) -> None:
            super(CreatePropertyRentedPaymentForm, self).__init__(*args, **kwargs)
            self.fields['rent_property'].widget.attrs['placeholder'] = 'Select Rent Property'
            self.fields['amount_paid'].widget.attrs['placeholder'] = "Enter amount"
            self.fields['payment_method'].widget.attrs['placeholder'] = "select method"
