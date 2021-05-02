
# external apis
class Khalti:

  def pay(self):
    print("Payment made through khalti app")

class Esewa:

  def payment(self):
    print("Payment done with Esewa")

class IMEPay:

  def make_payment(self):
    print("Payment made using IMEPAY")


# external apis end


import time
def sleeper():
  #sleeper method is to mimic delay in Transaction
  time.sleep(1)
  print("########")
  time.sleep(1)
  print("####")
  time.sleep(1)
  print("#")
  time.sleep(2)


#Our Interface
from abc import ABC, abstractmethod


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

class PaymentPortals:
  #contains all  of the payment portal classess
  payment_portals_dict = {
    "K": KhaltiPortal,
    "E": EsewaPortal,
    "I": IMEPayPortal
  }

  def get_all_portals(self):
    return self.payment_portals_dict

class PaymentClass:
  def __init__(self):
    self.portal_dict = PaymentPortals()

    
  def get_payment_class(self, mode):
    #return the payment_class depending upon the mode
    pay_classess = self.portal_dict.get_all_portals()

    if mode not in pay_classess.keys():
      raise Exception("Invalid Mode")
    else:
      payment_class = pay_classess.get(mode)
      return payment_class



class PaymentService:

  def make_payment(self, mode):
    method = mode.upper()
    payment_class_obj = PaymentClass()
    payment_class = payment_class_obj.get_payment_class(method)
    payment_class().pay()

class Transaction:
  def __init__(self, mode):
    print("Transaction is taking place")
    self.mode = mode
    self.payment_service = PaymentService()

  def transact(self):
    self.payment_service.make_payment(self.mode)



def run():
  print(f"Input the mode of payment \n")
  print("For Khati  press 'k'")
  print("For IMEPay press 'i'")
  print("For Esewa  press 'e'\n")
  val = input("Enter you value: ")
  Transaction(val).transact()

run()