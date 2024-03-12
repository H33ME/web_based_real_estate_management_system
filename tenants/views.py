from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from django.contrib import messages
# Create your views here.
from property.views import PropertyBaseView
from tenants.tenants_handler import TenantHandler
from property.property_handler import PropertyHandler
from tenants.forms import CreateNewUserAsTenantForm, LoginForm, EditTenantProfileForm, RentPropertyForm
from tenants.models import OccupationChoices

class CreateNewUserAsTenantView(PropertyBaseView):
    def get(self, request, *args, **kwargs):
        tenant_handler = TenantHandler()
        self.context_dict['form'] = CreateNewUserAsTenantForm()
        self.context_dict['occupation_choices'] = OccupationChoices.choices
        return render(request, 'accounts/register.html', self.context_dict)
    def post(self, request, *args, **kwargs):
        tenant_handler = TenantHandler()
        form = CreateNewUserAsTenantForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user, tenant = tenant_handler.create_new_user_as_tenant(data)

            messages.success(request, 'You have signed in successfully.')
            return redirect(reverse('login'))
        else:
            self.context_dict['form'] = form
            import pdb
            pdb.set_trace()
            return render(request, 'accounts/register.html', self.context_dict)
class LoginView(PropertyBaseView):

    def get(self, request):
        tenant_handler = TenantHandler()
        self.context_dict['form'] = LoginForm()
        return render(request, 'accounts/login.html', self.context_dict)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'you have login successfully.')
                return redirect(reverse('home'))
        else:
            self.context_dict['form'] = form
            return render(request, 'accounts/login.html', self.context_dict)

class LogOutView(PropertyBaseView):
    def get(self, request):
        logout(request)
        messages.success(request, 'you have logged out successfully.')
        return redirect(reverse("login"))

class TenantEditProfileView(PropertyBaseView):
    def get(self, request,  *args, **kwargs):
        tenant_handler = TenantHandler()
        data={
            'tenant_id':request.user.tenant.id
        }
        self.context_dict['form'] = EditTenantProfileForm()
        self.context_dict['occupation_choices'] = OccupationChoices.choices
        self.context_dict['tenant_id'] = request.user.tenant.id
        self.context_dict['tenant'] = tenant_handler.get_tenant_by_id(data)
        return render(request, 'accounts/edit-tenant-profile.html', self.context_dict)

    def post(self, request, *args, **kwargs):
        tenant_handler = TenantHandler()
        form = EditTenantProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['tenant_id'] = request.user.tenant.id
            tenant_handler.edit_tenant(data)
            return redirect(reverse('home'))
        else:
            self.context_dict['form'] = form
            return render(request, 'accounts/edit-tenant-profile.html', self.context_dict)
