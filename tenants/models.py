from django.db import models, transaction, IntegrityError

from django.contrib.auth.models import User
from django.db.models import Q
from phonenumber_field.modelfields import PhoneNumberField
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from property.models import Property, DEFAULT_STRING_VALUE
# Create your models here.
class OccupationChoices(models.TextChoices):
    STUDENT = 'Student', 'Student',
    TEACHER = 'Teacher', 'Teacher',
    ENGINEER = 'Engineer', 'Engineer',
    DOCTOR = 'Doctor', 'Doctor',
    ARTIST = 'Artist', 'Artist',
    BUSINESS_OWNER = 'Business Owner', 'Business Owner',
    FREELANCER = 'Freelancer', 'Freelancer',
    OTHER = 'Others', 'Others'

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name = 'tenant')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)
    identification_number = models.CharField(max_length=8, unique=True, null=False, blank=False, verbose_name='id_no', help_text='This is the identification number of the tenant')
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True)
    occupation = models.CharField(max_length = 100, choices=OccupationChoices.choices, default = OccupationChoices.OTHER)
    emergency_contact = models.CharField(max_length = 100, blank=True, null=True)


    class Meta:
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class RentProperty(models.Model):
    property = models.ForeignKey(Property, on_delete= models.CASCADE, related_name = 'property_rented')
    tenant = models.ForeignKey(Tenant, on_delete = models.CASCADE, related_name = 'tenant_renting_property')
    move_in_date = models.DateField(null=False, blank=False)
    lease_start_date = models.DateField(null=False, blank=False)
    lease_end_date = models.DateField(null=False, blank=False)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    payment_frequency = models.CharField(max_length=50, default= DEFAULT_STRING_VALUE)
    additional_notes = models.TextField(blank=True, default=DEFAULT_STRING_VALUE)

    class Meta:
        verbose_name = 'Rent Property'
        verbose_name_plural = 'Rent Properties'

    def __str__(self):
        return f"{self.tenant.first_name} {self.tenant.last_name} - {self.property.name}"

class TenantManager:
    def create_new_user_as_tenant(self, data):
        """
        This method creates a new tenant
        :param data:{
            'first_name':'first name of the tenant',
            'last_name':"last name of the tenant"
            'email':'email of the tenant',
            'identification_number':'the national identification number of tenant',
            'phone_number':'phone number  of the tenant',
            'occupation':'tenant occupation',

        }
        """
        user = User.objects.create(
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
        )
        if data.get('username'):
            user.username = data.get('username')

        user.set_password(data.get('password1'))
        user.save()
        # Create a new tenant associated with the user
        tenant_data = {
            'user': user,
            'first_name': data.get('first_name'),
            'last_name':data.get('last_name'),
            'identification_number': data.get('identification_number'),
            'phone_number': data.get('phone_number'),
            'occupation':data.get('occupation'),
            'emergency_contact':data.get('emergency_contact')
        }

        with transaction.atomic():
            # Use transaction to ensure both user and passenger are saved or none
            tenant = Tenant.objects.create(**tenant_data)

        return user, tenant

    def get_all_tenants(self, data):
        """
        This method returns all tenants
        :param data: {
            'page':1
        }
        :return:
        """
        results = self.filter_tenant(data)
        page = data.get('page', 1)
        paginator = Paginator(results, 20)
        try:
            tenant = paginator.page(page)
        except PageNotAnInteger:
            tenant = paginator.page(1)
        except EmptyPage:
            tenant = paginator.page(paginator.num_pages)
        return tenant

    def filter_tenant(self, data: dict):
        """
        This method filters tenant
        :param data: {
            'first name':'',
            'last name':'',
        }
        :return:
        """
        filters = {}

        if data.get('first_name'):
            filters['first_name__icontains'] = data.get('first_name')
        if data.get('last_name'):
            filters['last_name__icontains'] = data.get('last_name')
        return Tenant.objects.filter(**filters).order_by('id')

    def edit_tenant(self, data):
        """
        This method edit a tenant
        :param data: {
            'first name':'',
            'last name':'',
            'email':'',
            'phone number':'',
            'identification_number; '',
            'occupation':'',
            'emergency contact':'',
        }
        :return:tenant
        """
        edit_tenant_by_id = Tenant.objects.get(id=data.get('tenant_id'))
        edit_tenant_by_id.first_name = data.get('first_name')
        edit_tenant_by_id.last_name = data.get('last_name')
        edit_tenant_by_id.email = data.get('email')
        edit_tenant_by_id.phone_number = data.get('phone_number')
        edit_tenant_by_id.identification_number = data.get('identification_number')
        edit_tenant_by_id.emergency_contact = data.get('emergency_contact')
        edit_tenant_by_id.occupation = data.get('occupation')
        edit_tenant_by_id.save()
        return edit_tenant_by_id

    def get_tenant_by_id(self, data):
        """
        This method get tenant by id
        :param data: {
            'tenant_id':'',
        }
        :return:
        """
        return Tenant.objects.get(id = data.get('tenant_id'))

    def tenant_rent_property(self, data):
        tenant_id = data.get('tenant_id')
        property_id = data.get('property_id')
        move_in_date = data.get('move_in_date')
        lease_start_date = data.get('lease_start_date')
        lease_end_date = data.get('lease_end_date')

        try:
            # Retrieve Tenant and Property instances
            tenant = Tenant.objects.get(id=tenant_id)
            property = Property.objects.get(id=property_id)

            # Check if the property is available for rent
            if property.number_available <= 0:
                raise ValueError("The selected property is not available for rent.")

            # Check if the tenant has an existing rent record for the same property
            existing_rent_record = RentProperty.objects.filter(tenant=tenant, property=property).exists()
            if existing_rent_record:
                raise ValueError("The tenant already has an existing rent record for this property.")

            # Check if the provided dates are valid
            if lease_start_date < move_in_date or lease_end_date < lease_start_date:
                raise ValueError("Invalid date range provided.")

            # Create the RentProperty instance
            rent_property = RentProperty.objects.create(
                tenant=tenant,
                property=property,
                move_in_date=move_in_date,
                lease_start_date=lease_start_date,
                lease_end_date=lease_end_date,
                payment_frequency = data.get('payment_frequency'),
                additional_notes = data.get('additional_notes'),
                security_deposit = data.get('security_deposit'),
                rent_amount = data.get('rent_amount')
            )

            # Update the availability of the property
            property.number_available -= 1
            property.save()

            return rent_property

        except Tenant.DoesNotExist:
            raise ValueError("Tenant with the provided ID does not exist.")
        except Property.DoesNotExist:
            raise ValueError("Property with the provided ID does not exist.")
        except IntegrityError:
            raise ValueError("An integrity error occurred while creating the rent record.")
    def get_all_property_rented(self, data):
        """
        This method returns all property rented
        :param data: {
            'page':1
        }
        :return:
        """
        tenant = Tenant.objects.get(id=data.get('tenant_id'))
        return RentProperty.objects.filter(tenant = tenant)
