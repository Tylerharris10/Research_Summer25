import numpy as np
import os


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age}."
    
    def intro(self):
        print("Hi my name is " + self.name)

    def liscenseInfo(self):
        age = str(self.age)
        print(self.name + "(" + age + ")")
    
p1 = Person('Tyler', 20)
print(p1)
p1.intro()
p1.liscenseInfo()

del p1.age
p1.age = 40
print(p1.age)

class Car:

    def __init__(self, brand, model, numSeats, currentSpeed):
        self.brand = brand
        self.model = model
        self.numSeats = numSeats
        self.currentSpeed = currentSpeed
    
    def __str__(self):
        return f"{self.brand}({self.model})({self.numSeats})({self.currentSpeed})"
    
    def speeding(self):
        if self.currentSpeed > 65:
            return True
        else:
            return False
    def isSporty(self):
        if self.numSeats == 2:
            return True
        else:
            return False

porsche = Car('Porsche', 'Boxster', 2, 200)
print(porsche)
print(porsche.speeding())
print(porsche.isSporty())
del porsche.currentSpeed
porsche.currentSpeed = 40
print(porsche.speeding())
del porsche.numSeats
porsche.numSeats = 4
print(porsche.isSporty())