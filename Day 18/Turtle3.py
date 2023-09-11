import random
from turtle import *

tom = Turtle()
screen = Screen()
screen.colormode(255)
tom.speed(0)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw(size):
    for i in range(int(360 / size)):
        tom.color(change_color())
        tom.circle(200)
        tom.setheading(tom.heading() + size)


draw(15)
screen.exitonclick()
