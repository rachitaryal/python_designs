#Our Interface
from abc import ABC, abstractmethod
import time
from external_apis import Khalti, Esewa, IMEPay
from sleeper_module import sleeper



class PaymentPortalInterface(ABC):

  @abstractmethod
  def pay(self):
    #method to make payment
    pass


class KhaltiPortal(PaymentPortalInterface):
  def __init__(self):
    time.sleep(1)
    print("Processing Khalti Payment Portal...please wait\n")
    sleeper()
    self.main = Khalti()

  def pay(self):
    self.main.pay()
    


class EsewaPortal(PaymentPortalInterface):
  def __init__(self):
    time.sleep(1)
    print("Processing Esewa Payment Portal...please wait\n")
    sleeper()
    self.main = Esewa()

  def pay(self):
    self.main.payment()


class IMEPayPortal(PaymentPortalInterface):
  def __init__(self):
    time.sleep(1)
    print("Processing IMEPay Payment Portal...please wait\n")
    sleeper()
    self.main = IMEPay()

  def pay(self):
    self.main.make_payment()


#Our interface end