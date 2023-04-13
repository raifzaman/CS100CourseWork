'''
Raif Zaman
CS 100
HW 04
'''
import turtle

a = 3
b = 4
c = 5

#Question 1
if a < b:
    print("OK")

if c < b:
    print("OK")

if a + b == c:
    print("OK")

if a**2 + b**2 == c**2:
    print("OK")


#Question 2
if a < b:
    print("OK")
else:
    print('NOT OK')

if c < b:
    print("OK")
else:
    print('NOT OK')

if a + b == c:
    print("OK")
else:
    print('NOT OK')
if a**2 + b**2 == c**2:
    print("OK")
else:
    print('NOT OK')

#Question 3
screen = turtle.Screen()
drawing = turtle.Turtle()

width = None
while not width:
    try:
        width = int(input('Enter a width: '))
    except ValueError:
        print("Enter a valid integer")

length = None
while not length:
    try:
        length = int(input('Enter a length: '))
    except ValueError:
        print("Enter a valid integer.")



color = None
while not color:
    color = input('Enter a color: ')
    try:
        drawing.pencolor(color)
    except:
        print('Enter a valid color: ')
        color = None

shape = None
while not shape:
    shape = input('line, triangle, or square?: ')
    if shape not in ['line', 'triangle', 'square']:
        shape = None
        print("Error, ask for proper shape (line, triangle, or square?): ")

drawing.pensize(width)


if shape == 'line':
    turtle.getscreen()
    drawing.pendown()  # pen is on paper
    drawing.forward(length)
    turtle.exitonclick()
elif shape == 'triangle':
    window = turtle.getscreen()
    drawing.pendown()  # pen is on paper
    for i in range(3):  # for i in range 3 means code will be repeated three times
        drawing.forward(length)
        drawing.left(120)  # pen turns 120 degrees to create equilateral triangle
    turtle.exitonclick()
elif shape == 'square':
    window = turtle.getscreen()
    drawing.pendown()  # pen is on paper
    for i in range(4):
        drawing.lt(90)
        drawing.fd(length)
    turtle.exitonclick()



exit()