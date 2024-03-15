from payments.models import PaymentManager

class PaymentHandler:
    def __init__(self) -> None:
        self.payment_manager = PaymentManager()

    def create_rent_payment(self, data):
        """
        This method creates a rent_payments
        :param data: {
        }
        :return:
        """
        return self.payment_manager.create_rent_payment(data)

    def get_all_rent_payments(self, data):
        """
        This method returns all rent_payments
        :param data: {
            'page':1
        }
        :return:
        """
        return self.payment_manager.get_all_rent_payments(data)

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
        return self.payment_manager.edit_rent_payment(data)
    def get_rent_payment_by_id(self, data):
        """
        This method get rent_payment by id
        :param data: {
            'rent_payment_id':'',
        }
        :return:
        """
        return self.payment_manager.get_rent_payment_by_id(data)

    def edit_property_rent_transaction_status(self, data):
        """
        This method edit rent_payment by id
        :param data: {
            'rent_payment_id':'',
        }
        :return:
        """
        return self.payment_manager.edit_property_rent_transaction_status(data)

    def delete_tenant_rent_payment(self, data):
        """
        This method edit rent_payment by id
        :param data: {
            'rent_payment_id':'',
        }
        :return:
        """
        return self.payment_manager.delete_tenant_rent_payment(data)