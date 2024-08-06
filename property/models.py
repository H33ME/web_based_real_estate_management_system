from django.db import models
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
DEFAULT_STRING_VALUE = 'NOT AVAILABLE'

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
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
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
            property_type=data.get('property_type'),
            name = data.get('name'),
            description = data.get('description'),
            price=data.get('price'),
            bedrooms=data.get('bedrooms'),
            bathrooms=data.get('bathrooms'),
            location = data.get('location'),
            number_available = data.get('number_available')
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
        filters = Q()

        if data.get('keyword'):
             filters &= Q(name__icontains=data.get('keyword')) | Q(description__icontains=data.get('keyword'))

        if data.get("property_type"):
             filters &= Q(property_type_id=data.get("property_type"))

        if data.get("location"):
             filters &= Q(location=data.get("location"))

        if data.get('name'):
            filters['name__icontains'] = data.get('name')
        return Property.objects.filter(filters).order_by('-created_at')

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
        edit_property_by_id.price = data.get('price')
        edit_property_by_id.bathrooms = data.get('bathrooms')
        edit_property_by_id.bedrooms = data.get('bedrooms')
        edit_property_by_id.location = data.get('location')
        edit_property_by_id.number_available = data.get('number_available')
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
