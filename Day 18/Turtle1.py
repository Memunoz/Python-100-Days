import random
from turtle import *

turtle_t = Turtle()
turtle_t.shape("turtle")
colours = ["red", "blue", "green", "yellow", "orange", "purple"]


def square():
    for _ in range(4):
        turtle_t.forward(100)
        turtle_t.right(90)


def dashed():
    for _ in range(50):
        turtle_t.forward(5)
        turtle_t.penup()
        turtle_t.forward(5)
        turtle_t.pendown()


def shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle_t.forward(100)
        turtle_t.right(angle)


for forms in range(3, 11):
    turtle_t.color(random.choice(colours))
    shape(forms)


# square()
# dashed()

screen = Screen()
screen.exitonclick()
