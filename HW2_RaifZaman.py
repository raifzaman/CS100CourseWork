'''
#list exercise
#List lst is a list of prices for a pair of boots at different online retailers
lst = [159.99, 160.00, 205.95, 128.83, 175.49]
#You've found another retailer selling the boots for 160.00, add this price to list
lst.append(160.00)
#Compute the number of retailers selling the boots for 160.00
lst.count(160.00)
#Find the minimum price for the boots in lst
min(lst)
#Using c), find the index of the minimum price in lst
lst.index(128.83)
#Using c), remove the minimum price in lst
lst.remove(128.83)
#Sort list in increasing order
lst.sort()
print(lst)

#tuple exercise
p1 = ['do','it','better']
p2 = ['make','us','stronger']
print(p1[1:2])
lst = p2[:1] + p1[-2:]
print(lst)


#Exercise to practice importing libraries outside of python standard library
import math
# a) Print the length of the hypotenuse in a right triangle whose other two sides have lengths 3 and 4
c = math.sqrt(3**2+4**2)
print(c)
# b) Print the value of the Boolean expression that evaluates wether the length of the above hypotenuse is 5
c = math.sqrt(3**2+4**2) ==5
# c) The area of a disk of radius 10
print(math.pi * 10 **2)
# d) The value of the Boolean expression that checks wether a point with coordinates (5,5) is inside a circle with center (0,0) and radius 7
c = (2*5**2 < 7**2)
print(c)
'''

#Question 1
def gradeFrequency():
    grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']

    frequency = [grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('F')]

    print(frequency)

gradeFrequency()

#Output (When function is called): [4, 2, 2, 0, 2]

#Question 2A

dog_breeds = ['Collie','Sheepdog','Chow','Chihuahua']

print(dog_breeds)

#Question2B
herding_dogs = dog_breeds[0:2]

print(herding_dogs)

#Question2C
tiny_dogs = []
tiny_dogs.append(dog_breeds[-1])
print(tiny_dogs)

#2D
def persian():

    dog_breeds = ['Collie','Sheepdog','Chow','Chihuahua']
    i = 'Persian'
    if i in dog_breeds:
        print("True")
    else:
        print("False")

persian()