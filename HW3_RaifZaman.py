'''
Raif Zaman
CS 100
HW 03
'''

#Question 1
import turtle
def equilateralTriangle():
    window = turtle.Screen()
    turtle.pendown()  # pen is on paper
    for i in range(3): #for i in range 3 means code will be repeated three times
        turtle.forward(100)
        turtle.left(120) #pen turns 120 degrees to create equilateral triangle

    turtle.exitonclick()


def square100():
    square = turtle.Turtle()
    window = turtle.getscreen()
    for i in range(4):
        square.lt(90)
        square.fd(100)

    turtle.exitonclick()

def pentagon100():
    pentagon = turtle.Turtle()
    for i in range(5):
        pentagon.left(72)
        pentagon.forward(100)


    turtle.exitonclick()


# Question 2
def concentric_Circle():
    Con_Circle = turtle.Turtle()
    # for loop to draw the 4 circles
    for radius in [50, 100, 150, 200]:
        Con_Circle.penup()
        Con_Circle.goto(0, -radius)
        Con_Circle.pendown()
        Con_Circle.circle(radius)

    turtle.exitonclick()


#Question 3
import math
def mathFactorial():
    x = 100
    print("The factorial of 100 is: ")
    print(math.factorial(x))

def logFunction():
    x = 1000000
    print("The log (base 2) of 1,000,000 is: ")
    print(math.log2(x))

def greatest_common_divisor():
    a = 63
    b = 49
    print("The greatest common divisor of 63 and 49 is: ")
    print(math.gcd(a,b))

