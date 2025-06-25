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
