'''
Raif Zaman
CS 100
HW 05
'''

import math

#Question 1
def months():
    months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
    for i in months:
        if i.startswith('J'):
            print(i)

#Question 2
def integers():
    for i in range(100):
        if i % 2 == 0 and i % 5 == 0:
            print(i)

#Question 3
def horton():
    horton = "A person's a person, no matter how small."
    vowels = 'aeiouAEIOU'
    for letters in horton:
        if letters in vowels:
            print(letters)

