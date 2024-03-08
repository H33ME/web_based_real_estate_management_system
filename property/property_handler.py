from property.models import PropertyManager

class PropertyHandler:
    def __init__(self):
        self.property_manager = PropertyManager()

    def create_property(self, data):
        """
        This method creates a new property
        :param data:{
            'title':'title of the property',
            'description':'description of the property',
            'price':'price of the property',
            'bedroom':'bedrooms available',
            'bathroom':'bathroom available',
            'location':'the property location'
        }
        """
        return self.property_manager.create_property(data)

    def get_all_property(self, data):
        """
        This method returns all property
        :param data: {
            'page':1
        }
        :return:
        """
        return self.property_manager.get_all_property(data)

    def get_property_by_id(self, data):
        """
        This method get property by id
        :param data: {
            'property_id':'',
        }
        :return:
        """
        return self.property_manager.get_property_by_id(data)

    def filter_property(self, data):
        """
        This method filters property
        :param data: {
            'title':'',
        }
        :return:
        """
        return self.property_manager.filter_property(data)

    def edit_property(self, data):
        """
        This method edit a property
        :param data: {
            'title':'',
            'description':'',
            'price':'',
            'bathrooms':'',
            'bedrooms':'',
            'location':'',
        }
        :return:Property
        """
        return self.property_manager.edit_property(data)

    def get_all_property_types(self, data):
        """
        This method get all property types
        :param data: {
            'page':1,
        }
        :return:
        """
        return self.property_manager.get_all_property_types(data)

    def create_property_type(self, data):
        """
        This method get creates property types
        :param data: {
            'name':'',
        }
        :return:
        """
        return self.property_manager.create_property_type(data)

    def edit_property_type(self, data):
        """
        This method edits property types
        :param data: {
            'name':'',
        }
        :return:
        """
        return self.property_manager.edit_property_type(data)

    def get_property_type_by_id(self, data):
        """
        This method returns property type by id
        :param data:{
        'property_type_id':'id of the property type'
        }
        :return:
        """
        return self.property_manager.get_property_type_by_id(data)

    def delete_property_type(self, data):
        """
        This method delete property type by id
        :param data:{
        'property_type_id':'id of the property type'
        }
        :return:
        """
        return self.property_manager.delete_property_type(data)

    def delete_property(self, data):
        """
        This method delete property
        :param data:{
        'property_id':'id of the property'
        }
        :return:
        """
        return self.property_manager.delete_property(data)