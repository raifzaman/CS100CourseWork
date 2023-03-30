'''
Raif Zaman
CS 100
HW 01
'''

''''
age = 18
length = 5.10
name = 'Raif Zaman'

#1.1
print("Hello World"
Output: 
    print("Hello World"
         ^
SyntaxError: '(' was never closed

print ("Hello World)
Output: 
    print ("Hello World)
           ^
SyntaxError: unterminated string literal (detected at line 12)

print(+2)

Output: 2 

print(2++2)

Output: 4

print(02)
Output:    
    print(02)
          ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

print(2 2)
Output:
    print(2 2)
          ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

#1-2
a = 42*60
b = 42

c = a+b
print(c)
Output: 2562
#There are 2562 seconds in 42 minutes and 42 seconds 

a = 1.61
b = 10
c = b/a

print(c)
Output: 6.211180124223602

a = 42
b = 42
totalTime = (a*60) + b

miles = 10
milesperKm = 1.61

totalDistance = miles / milesperKm

AverageSpeed = (totalDistance / totalTime)*3600 #3600 = 60 minutes converted to seconds

print(AverageSpeed)

Output: 8.727653570337614

#2-1
n = 42
42 = n
Output: 
42 = n
    ^^^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

print(x=y=1)
Output: 
 print(x=y=1)
             ^
SyntaxError: invalid syntax

age = 18; name = 'Raif' #Using a semicolon at the end of a python statement allows you to write multiple statements on the same line of code

age = 18 name = 'Raif'
Output:
    age = 18 name = 'Raif'
             ^^^^
SyntaxError: invalid syntax

Height = 5.5
Output:
    Height = 5.5.
                 ^
SyntaxError: invalid syntax

x = 4
y = 2
print(xy)
Output:
    print(xy)
          ^^
NameError: name 'xy' is not defined. Did you mean: 'x'?
#Without using the proper math function, the IDE read 'xy' as a variable and since 'xy' is not defined it gave back a name error

Exercise 2-2
1. 
import math
radius = 5
Volume = 4/3*math.pi*radius**3
print("The volume of a sphere with a radius of 5 is: ", Volume)
2. 
Costof60books = (24.95*0.60)*60
ShippingforBookNum1 = 3.00
ShippingforRestofBooks = 0.75*59

TotalCost = Costof60books + ShippingforBookNum1 + ShippingforRestofBooks

print("The total wholesale cost for 60 books is: ", TotalCost)
3. 
start_time = (6*60 + 52)*60
easyPace = (8*60 + 15)*2
tempoPace = (7*60 + 12)*3

breakfast_hour = (start_time + easyPace + tempoPace)/(60*60)
breakfast_int_hour = int(breakfast_hour)

breakfast_minute  = (breakfast_hour - breakfast_int_hour)*60
breakfast_int_minute = int(breakfast_minute)

print("Breakfast is at", breakfast_int_hour,":",breakfast_int_minute)
'''
