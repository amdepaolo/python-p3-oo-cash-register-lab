#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = None

  def add_item(self, item, price, quantity = 1):
    quant_price = price * quantity
    self.total += quant_price
    for i in range(quantity): 
      self.items.append(item)
    self.last_transaction = {"item": item, "price": price, "quantity": quantity}

  def apply_discount(self):
    if self.discount == 0:
      print(  "There is no discount to apply.")
    else:
      total = self.total  
      removed = total * (self.discount / 100)
      self.total = total - removed
      print(f"After the discount, the total comes to ${self.total:.0f}.")
  
  def void_last_transaction(self):
    if self.last_transaction:
      last_tr = self.last_transaction
      item = last_tr["item"]
      price = last_tr["price"]
      quantity = last_tr["quantity"]
      self.total -= price*quantity
      for i in range(quantity):
        self.items.pop()
    
