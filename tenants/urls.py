from django.urls import path

from tenants.views import CreateNewUserAsTenantView, LoginView, LogOutView, \
    TenantEditProfileView

urlpatterns = [
    path('register/', CreateNewUserAsTenantView.as_view(), name = 'register_tenant'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogOutView.as_view(), name = 'logout'),
    path('edit_tenant_profile/<int:tenant_id>/', TenantEditProfileView.as_view(), name = 'edit_tenant_profile'),
]
