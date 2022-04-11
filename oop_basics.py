# -*- coding: utf-8 -*-
"""oop-basics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ALMFQg3h_C-8-1wRI3X8em3rIhcw32mf
"""

class Car:
  def __init__(self):
    Car.price = 100000

  def sell(self):
    print("Selling price of the car is {}".format(Car.price))

  def setprice(self,price):
    Car.price = price

tesla = Car()
tesla.sell()

tesla.price = 500000
tesla.sell()

#this is encapsulation. the variable price is a private variable of the class Car and cant be changed from outside

tesla.setprice(50000)
tesla.sell()
#here with the help of setter method which is the part of the class, the private variable can be changed

#inheritance
class Tesla(Car):
  def __init__(self):
    super().__init__()
    Tesla.price = 900000
    print("Tesla is ready")

  def fuel(self):
    print("Tesla uses Electricity.")

modX = Tesla()
modX.sell()

modX.setprice(900000)
modX.sell()
#Inheritance

class Audi(Car):
  def __init__(self):
    super().__init__()
    Audi.price = 800000
    print("Audi is ready")

  def fuel(self):
    print("Audi uses Petrol.")

def get_fuel(car):
  car.fuel()

modS = Tesla()
q8 = Audi()

get_fuel(modS)
get_fuel(q8)
#2 subclasses of car have sam efuel function, which is being accesssed by a common interface known as get_fuel.