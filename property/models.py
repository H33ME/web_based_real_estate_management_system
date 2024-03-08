from django.db import models
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
DEFAULT_STRING_VALUE = 'NOT AVAILABLE'
PRICE_CHOICES = [
    (5000, 'Sh. 5000'),
    (10000, 'Sh. 10,000'),
    ( 30000,'Sh. 30000'),
    (50000, 'Sh. 50000')
]

BEDROOM_CHOICES = [
    (0, 'Single Room'),
    (1, '1 Bedroom'),
    (2, '2 Bedrooms'),
    (3, '3 Bedrooms'),
    # Add more options as needed
]

BATHROOM_CHOICES = [
    (0, 'Single Room'),
    (1, '1 Bathroom'),
    (2, '2 Bathrooms'),
    (3, '3 Bathrooms'),
    # Add more options as needed
]

# Create your models here.
class PropertyType(models.Model):
    name = models.CharField(
        max_length=15,
        default=DEFAULT_STRING_VALUE,
        null=True, blank=True
    )
    class Meta:
        verbose_name = 'Property type'
        verbose_name_plural = 'Property types'

    def __str__(self):
        return self.name

class Property(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True, blank=True,
                                        related_name='property')
    name = models.CharField(max_length=1000, default=DEFAULT_STRING_VALUE, null=True, blank=True)
    description = models.TextField(max_length = 1000, default = DEFAULT_STRING_VALUE, null = True, blank = True)
    number_available = models.PositiveIntegerField(default=0, verbose_name='properties available',
                                        help_text='This is the number of property available')
    price = models.IntegerField(choices=PRICE_CHOICES,)
    bedrooms = models.IntegerField(choices=BEDROOM_CHOICES)
    bathrooms = models.IntegerField(choices=BATHROOM_CHOICES)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name

class PropertyManager:
    def create_property(self, data):
        """
        This method creates a new property
        :param data:{
            'name':'name of the property',
            'description':'description of the property',
            'price':'price of the property',
            'bedroom':'bedrooms available',
            'bathroom':'bathroom available',
            'location':'the property location'
        }
        """
        return Property.objects.create(
            property_type_id=data.get('property_type_id'),
            name = data.get('name'),
            description = data.get('description'),
            price=data.get('price'),
            bedrooms=data.get('bedrooms'),
            bathrooms=data.get('bathrooms'),
            location = data.get('location')
        )

    def get_all_property(self, data):
        """
        This method returns all property
        :param data: {
            'page':1
        }
        :return:
        """
        results = self.filter_property(data)
        page = data.get('page', 1)
        paginator = Paginator(results, 20)
        try:
            property = paginator.page(page)
        except PageNotAnInteger:
            property = paginator.page(1)
        except EmptyPage:
            property = paginator.page(paginator.num_pages)
        return property

    def filter_property(self, data: dict):
        """
        This method filters property
        :param data: {
            'name':'',
        }
        :return:
        """
        filters = {}
        # Property search logic
        keyword = data.get('keyword')
        property_type_id = data.get('property_type')
        location_id = data.get('location')

        # Use Q objects to build a complex query based on selected values
        query = Q()

        if keyword:
            query &= Q(title__icontains=keyword) | Q(description__icontains=keyword)

        if property_type_id:
            query &= Q(property_type__id=property_type_id)

        if location_id:
            query &= Q(location__id=location_id)

        # Add the constructed query to the filters
        if query:
            filters.update({'query': query})
        if data.get('name'):
            filters['name__icontains'] = data.get('name')
        return Property.objects.filter(**filters).order_by('-created_at')

    def edit_property(self, data):
        """
        This method edit a property
        :param data: {
            'name':'',
            'description':'',
            'price':'',
            'bathrooms':'',
            'bedrooms':'',
            'location':'',
        }
        :return:Property
        """
        edit_property_by_id = Property.objects.get(id=data.get('property_id'))
        edit_property_by_id.name = data.get('name')
        edit_property_by_id.description = data.get('description')
        edit_property_by_id.bathrooms = data.get('bathrooms')
        edit_property_by_id.bedrooms = data.get('bedrooms')
        edit_property_by_id.location = data.get('location')
        edit_property_by_id.save()
        return edit_property_by_id

    def get_property_by_id(self, data):
        """
        This method get property by id
        :param data: {
            'property_id':'',
        }
        :return:
        """
        return Property.objects.get(id = data.get('property_id'))

    def get_all_property_types(self, data):
        """
        This method get all property types
        :param data: {
            'page':1,
        }
        :return:
        """
        results = PropertyType.objects.all().order_by('id')
        page = data.get('page', 1)
        paginator = Paginator(results, 20)
        try:
            property_types = paginator.page(page)
        except PageNotAnInteger:
            property_types = paginator.page(1)
        except EmptyPage:
            property_types = paginator.page(paginator.num_pages)
        return property_types

    def create_property_type(self, data):
        """
        This method updates the property type
        :param data: {
            'name':'',
        }
        :return:
        """
        property_type = PropertyType.objects.filter(name=data.get('name'))
        if property_type:
            property_type = property_type.first()
        else:
            property_type = PropertyType()
        property_type.name = data.get('name')
        property_type.save()
        return property_type


    def edit_property_type(self, data):
        """
        This method edits property types
        :param data: {
            'name':'',
        }
        :return:
        """
        property_type_by_id = PropertyType.objects.get(id=data.get('property_type_id'))
        property_type_by_id.name = data.get('name')
        property_type_by_id.save()
        return property_type_by_id

    def get_property_type_by_id(self, data):
        """
        This method returns property type by id
        :param data:{
        'property_type_id':'id of the property type'
        }
        :return:
        """
        return PropertyType.objects.get(id = data.get('property_type_id'))

    def delete_property_type(self, data):
        """
        This method delete property type by id
        :param data:{
        'property_type_id':'id of the property type'
        }
        :return:
        """
        property_type = PropertyType.objects.get(id=data.get('property_type_id'))
        property_type.delete()
        return property_type

    def delete_property(self, data):
        """
        This method delete property
        :param data:{
        'property_id':'id of the property'
        }
        :return:
        """
        property = Property.objects.get(id=data.get('property_id'))
        property.delete()
        return property