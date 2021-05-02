from payment_service import PaymentService


class Transaction:
  def __init__(self, mode):
    """ takes in the payment mode and initializes the payment service"""
    print("Transaction is taking place")
    self.mode = mode
    self.payment_service = PaymentService()

  def transact(self):
    """calls the payment service make_payment method """
    self.payment_service.make_payment(self.mode)