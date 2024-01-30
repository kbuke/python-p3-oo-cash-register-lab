#!/usr/bin/env python3

class CashRegister:
  def __init__(self,  discount = 0):
    self.discount = discount
    self.items = []
    self.total = 0

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for item_quantity in range(quantity):
      self.items.append(item)
    self.last_item_price = price * quantity
  
  def apply_discount(self):
    self.total = self.total - ((self.discount / 100) * self.total)
    if self.discount > 0:
      print (f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total -= (self.last_item_price)
    