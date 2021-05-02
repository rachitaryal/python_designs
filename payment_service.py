from payment_portals import  PaymentClass

class PaymentService:

  def make_payment(self, mode):
    """accepts a payment mode and makes payment"""
    method = mode.upper()
    payment_class_obj = PaymentClass()
    payment_class = payment_class_obj.get_payment_class(method)
    payment_class().pay()