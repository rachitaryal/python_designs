from transaction import Transaction



def run():
  print(f"Input the mode of payment \n")
  print("For Khati  press 'k'")
  print("For IMEPay press 'i'")
  print("For Esewa  press 'e'\n")
  val = input("Enter you value: ")
  Transaction(val).transact()

