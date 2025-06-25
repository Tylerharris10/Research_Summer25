import numpy as np
import os

def my_function(f_name, l_name):
    print(f_name + ' ' + l_name)

my_function('Tyler', 'Harris')

def my_kids(*kids):
    print("The youngest kid is named " + kids[3])

my_kids('Tyler', 'Hallie', 'Leighton', 'Foster')

def my_kids2(child1, child2, child3):
    print("The youngest kid is named " + child3)

my_kids2('Tyler','Hallie','Leighton')

def my_kids3(**kids):
    print("His last name is " + kids['lname'])

my_kids3(fname = 'Tyler', lname = 'Harris')

def my_country(country = 'USA'):
    print('I am from ' + country)

my_country()
my_country('Canada')

def my_kids4(kids):
    print("The youngest kid is " + kids[len(kids)-1])

kids = ['Tyler', 'Hallie', 'Leighton', 'Foster']
my_kids4(kids)

def my_food(food):
    shoppingList = ''
    for x in food: 
        shoppingList += x + ', '
    print(shoppingList)

food = ['Apple', 'Orange', 'Banana']
my_food(food)

def numbers(a, b, /, *, c, d):
    print(a + b + c + d)

numbers(3, 5, c = 7, d = 9)






