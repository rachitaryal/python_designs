from internal_apis.portal_interface import KhaltiPortal, EsewaPortal, IMEPayPortal


class PaymentPortals:
  """contains all  of the payment portal classess"""
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
    """return the payment_class depending upon the mode"""
    pay_classess = self.portal_dict.get_all_portals()

    if mode not in pay_classess.keys():
      raise Exception("Invalid Mode")
    else:
      payment_class = pay_classess.get(mode)
      return payment_class