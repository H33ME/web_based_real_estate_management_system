from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages

from property.property_handler import PropertyHandler
from property.forms import AddNewPropertyForm, EditPropertyTypeForm, EditPropertyForm
from property.models import BATHROOM_CHOICES, BEDROOM_CHOICES
# Create your views here.

class PropertyBaseView(View):
    """
    :Brief: Custom base class for django's class based views
    """
    def __init__(self, **kwargs):
        """ Initializes the base view object
        """

        self.context_dict = {

        }

        super(PropertyBaseView, self).__init__(**kwargs)

class PropertyHomePageView(PropertyBaseView):
    def get(self, request, *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        property_handler = PropertyHandler()
        data = {
            'page':request.GET.get('page', 1),
        }
        self.context_dict['property_types'] = property_handler.get_all_property_types(data)
        self.context_dict['properties'] = property_handler.get_all_property(data)
        return render(request, 'back-end/index.html', self.context_dict)

class PropertyView(PropertyBaseView):
    def get(self, request, *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        property_handler = PropertyHandler()
        data = {
            'page':request.GET.get('page', 1)
        }
        self.context_dict['properties'] = property_handler.get_all_property(data)
        return render(request, 'back-end/property.html', self.context_dict)

class AddNewPropertyView(PropertyBaseView):
    def get(self, request, *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        property_handler = PropertyHandler()
        data = {
            'page':request.GET.get('page', 1),
        }
        self.context_dict['property_types'] = property_handler.get_all_property_types(data)
        self.context_dict['properties'] = property_handler.get_all_property(data)
        self.context_dict['BEDROOM_CHOICES'] = BEDROOM_CHOICES
        self.context_dict['BATHROOM_CHOICES'] = BATHROOM_CHOICES
        self.context_dict['form'] = AddNewPropertyForm()
        return render(request, 'back-end/add-property.html', self.context_dict)

    def post(self, request, *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        property_handler = PropertyHandler()
        form = AddNewPropertyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            property_handler.create_property(data)
            messages.success(request, 'Property was created successfully!')
            return redirect(reverse('property'))
        else:
            self.context_dict['form'] = form
            return render(request, 'back-end/add-property.html', self.context_dict)

class PropertyAboutView(PropertyBaseView):
    def get(self,request, *args, **kwargs):
        return render(request, 'back-end/about.html', self.context_dict)

class PropertyTypeView(PropertyBaseView):
    def get(self, request, *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        property_handler = PropertyHandler()
        data = {
            'page':request.GET.get('page', 1),
        }
        self.context_dict['property_types'] = property_handler.get_all_property_types(data)
        return render(request, 'back-end/property-type.html', self.context_dict)

class PropertyAddPropertyTypeView(PropertyBaseView):

    def post(self, request, *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        property_handler = PropertyHandler()
        name = request.POST.get('name')
        data = {
            'name': name,
        }
        property_handler.create_property_type(data)
        messages.success(request, 'Property type has been created successfully')
        return redirect(reverse('property_type'))

class PropertyEditPropertyTypeView(PropertyBaseView):
    def get(self, request, property_type_id, *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        property_handler = PropertyHandler()
        data = {
            'property_type_id':property_type_id,
        }
        self.context_dict['form'] = EditPropertyTypeForm()
        self.context_dict['property_type'] = property_handler.get_property_type_by_id(data)
        self.context_dict['property_type_id'] = property_type_id
        return render(request,'back-end/edit-property-type.html', self.context_dict)

    def post(self, request, property_type_id,  *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        property_handler = PropertyHandler()
        form = EditPropertyTypeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['property_type_id'] = property_type_id
            property_handler.edit_property_type(data)
            messages.success(request, "Property type was edited successfully!")
            return redirect(reverse('property_type'))
        else:
            self.context_dict['form'] = form
            return render(request, 'back-end/edit-property-type.html', self.context_dict)

class PropertyEditPropertyView(PropertyBaseView):
    def get(self, request, property_id, *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        property_handler = PropertyHandler()
        data = {
            'property_id':property_id,
            'page':request.GET.get('page', 1)
        }
        self.context_dict['property'] = property_handler.get_property_by_id(data)
        self.context_dict['property_types'] = property_handler.get_all_property_types(data)
        self.context_dict['properties'] = property_handler.get_all_property(data)
        self.context_dict['form'] = EditPropertyForm()
        self.context_dict['property_id'] = property_id
        self.context_dict['BATHROOM_CHOICES'] = BATHROOM_CHOICES
        self.context_dict['BEDROOM_CHOICES'] = BEDROOM_CHOICES
        return render(request, 'back-end/edit-property.html', self.context_dict)

    def post(self, request, property_id, *args, **kwargs):
        """
        This filters the products table
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        property_handler = PropertyHandler()
        form = EditPropertyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['property_id'] = property_id
            property_handler.edit_property(data)
            messages.success(request, 'Property was edited successfully.')
            return redirect(reverse('property'))
        else:
            self.context_dict['form'] = form
            import pdb
            pdb.set_trace()
            return render(request, 'back-end/edit-property.html', self.context_dict)

class PropertyDeletePropertyTypeView(PropertyBaseView):
    def get(self, request,property_type_id, *args, **kwargs):
        property_handler = PropertyHandler()
        data = {
            'property_type_id':property_type_id
        }
        property_handler.delete_property_type(data)
        messages.success(request, "Property Type has been deleted successfully.")
        return redirect(reverse('property_type'))

class PropertyDeletePropertyView(PropertyBaseView):
    def get(self, request,property_id, *args, **kwargs):
        property_handler = PropertyHandler()
        data = {
            'property_id':property_id
        }
        property_handler.delete_property(data)
        messages.success(request, "Property has been deleted successfully.")
        return redirect(reverse('property'))
