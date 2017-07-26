from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
t.penup()
t.setposition(x_pos, y_pos)

### Write your code below:

color = input('What color do you want your shape? ')
t.pencolor(color)

sides = input("Enter a number: ")
x = int(sides)
ex_angle = 180-((180*(sides-2)/sides))

# t.pendown()

t.pendown()
for loop in range(4):
    t.right(90)
    t.forward(100)

setup(500,300)
x_pos = -150
y_pos = -100
t.penup()
t.setposition(x_pos, y_pos)

t.pendown()
for loop in range(3):
    t.right(120)
    t.forward(100)



exitonclick()
