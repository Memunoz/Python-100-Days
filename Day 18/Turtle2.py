import random
from turtle import *

tom = Turtle()
screen = Screen()
screen.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def random_walk(walk):
    tom.pensize(10)
    tom.speed(0)
    Angles = [0, 90, 180, 270]
    last_move = random.choice(Angles)

    for i in range(walk):
        tom.color(change_color())
        tom.forward(25)

        possible_angles = [angle for angle in Angles if angle != last_move]
        next_move = random.choice(possible_angles)

        last_move = next_move
        tom.setheading(next_move)


random_walk(2000)
screen.exitonclick()
