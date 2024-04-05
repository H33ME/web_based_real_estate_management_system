import uuid
from django.db import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from tenants.models import RentProperty, Tenant

class PaymentMethodChoices(models.TextChoices):
        CASH = 'cash', 'Cash'
        CHECK = 'check', 'Check'
        BANK_TRANSFER = 'bank_transfer', 'Bank Transfer'
        ONLINE_PAYMENT = 'online_payment', 'Online Payment'
        MPESA = 'mpesa', 'M-PESA'
        OTHER = 'other', 'Other'

class TransactionChoices(models.TextChoices):
    COMPLETE = 'complete', "Complete"
    PENDING = 'pending', 'Pending'
    INCOMPLETE = 'incomplete', 'Incomplete'

class RentPayment(models.Model):

    rent_property = models.ForeignKey(RentProperty, on_delete=models.CASCADE, related_name='rent_payments')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=100, choices=PaymentMethodChoices, default=PaymentMethodChoices.CASH)
    payment_reference = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    transaction_status = models.CharField(max_length = 100, choices = TransactionChoices, default=TransactionChoices.PENDING)

    class Meta:
        verbose_name = 'Rent Payment'
        verbose_name_plural = 'Rent Payments'

    def __str__(self):
        return f"Payment of sh {self.amount_paid} for {self.rent_property.property.name} rented by {self.rent_property.tenant.first_name}"

    @property
    def balance(self):
        return int(self.rent_property.property.price) - int(self.amount_paid)

class PaymentManager:
     def create_rent_payment(self, data):
          return RentPayment.objects.create(
               rent_property = data.get('rent_property'),
               amount_paid = data.get('amount_paid'),
               payment_method = data.get('payment_method'),
          )

     def get_all_rent_payments(self, data):
        """
        This method returns all rent_payments
        :param data: {
            'page':1
        }
        :return:
        """
        results = RentPayment.objects.all()
        page = data.get('page', 1)
        paginator = Paginator(results, 20)
        try:
            rent_payment = paginator.page(page)
        except PageNotAnInteger:
            rent_payment = paginator.page(1)
        except EmptyPage:
            rent_payment = paginator.page(paginator.num_pages)
        return rent_payment

     def edit_rent_payment(self, data):
        """
        This method edit a rent_payment
        :param data: {
            'amount_paid:'',
            'payment_date':'',
            'payment_method':'',
            'payment_reference':'',
            'transaction_status',:'',
        }
        :return:rent_payment
        """
        edit_rent_payment_by_id = RentPayment.objects.get(id=data.get('rent_payment_id'))
        edit_rent_payment_by_id.amount_paid = data.get('amount_paid')
        edit_rent_payment_by_id.payment_date = data.get('payment_date')
        edit_rent_payment_by_id.payment_method = data.get('payment_method')
        edit_rent_payment_by_id.payment_reference = data.get('payment_reference')
        edit_rent_payment_by_id.transaction_status = data.get('transaction_status')
        edit_rent_payment_by_id.rent_property = data.get('rent_property')
        edit_rent_payment_by_id.save()
        return edit_rent_payment_by_id

     def get_rent_payment_by_id(self, data):
        """
        This method get rent_payment by id
        :param data: {
            'rent_payment_id':'',
        }
        :return:
        """
        return RentPayment.objects.get(id = data.get('rent_payment_id'))

     def edit_property_rent_transaction_status(self, data):
        rent_payment = RentPayment.objects.get(id = data.get('rent_payment_id'))
        rent_payment.transaction_status = data.get('transaction_status')
        rent_payment.save()
        return rent_payment

     def delete_tenant_rent_payment(self, data):
        """
        This method delete rent_payment by id
        :param data: {
            'rent_payment_id':'',
        }
        :return:
        """
        rent_payment = RentPayment.objects.get(id=data.get('rent_payment_id'))
        rent_payment.delete()
        return rent_payment
