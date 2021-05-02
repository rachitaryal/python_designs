from payment_service import PaymentService


class Transaction:
  def __init__(self, mode):
    print("Transaction is taking place")
    self.mode = mode
    self.payment_service = PaymentService()

  def transact(self):
    self.payment_service.make_payment(self.mode)