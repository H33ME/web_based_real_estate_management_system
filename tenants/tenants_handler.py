from tenants.models import TenantManager

class TenantHandler:
    def __init__(self):
        self.tenant_manager = TenantManager()

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
        return self.tenant_manager.create_new_user_as_tenant(data)

    def get_all_tenants(self, data):
        """
        This method returns all tenant
        :param data: {
            'page':1
        }
        :return:
        """
        return self.tenant_manager.get_all_tenants(data)

    def filter_tenant(self, data: dict):
        """
        This method filters tenant
        :param data: {
            'first name':'',
            'last name':'',
        }
        :return:
        """
        return self.tenant_manager.filter_tenant(data)

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
        return self.tenant_manager.edit_tenant(data)
    def get_tenant_by_id(self, data):
        """
        This method get tenant by id
        :param data: {
            'tenant_id':'',
        }
        :return:
        """
        return self.tenant_manager.get_tenant_by_id(data)

    def tenant_rent_property(self, data):

        return self.tenant_manager.tenant_rent_property(data)

    def get_all_property_rented(self, data):
        """
        This method returns all property rented
        :param data: {
            'page':1
        }
        :return:
        """
        return self.tenant_manager.get_all_property_rented(data)
    def get_property_rented_by_id(self, data):
        """
        This method returns all property rented per id
        :param data: {
            'property_rented_id':''
        }
        :return:
        """
        return self.tenant_manager.get_property_rented_by_id(data)

    def delete_tenant(self, data):
        return self.tenant_manager.delete_tenant(data)

    def notify_tenant_to_pay_rent(self, data):
        return self.tenant_manager.notify_tenant_to_pay_rent(data)

    def generate_room_numbers(self, data):
        return self.tenant_manager.generate_room_numbers(data)
