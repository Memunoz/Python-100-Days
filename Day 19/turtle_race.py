from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win? Pick a color"
)
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
y_positions = [-250, -150, -50, 50, 150, 250]
all_turtles = []

# Crear las tortugas y agregarlas a la lista all_turtles
for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-300, y=y_positions[i])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

winning_turtle = None  # Variable para almacenar la tortuga ganadora

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 320:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                winner_text = f"You've won! The {winning_color} turtle is the winner!"
            else:
                winner_text = f"You've lost! The {winning_color} turtle is the winner!"
            # Mostrar el mensaje del ganador en la pantalla en la coordenada Y=50
            winner_display = Turtle()
            winner_display.penup()
            winner_display.goto(0, 50)
            winner_display.color("white")  # Configurar el color del texto en blanco
            winner_display.write(
                winner_text, align="center", font=("Arial", 24, "normal")
            )
            # Almacenar la tortuga ganadora
            winning_turtle = turtle

        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)

# Llevar la tortuga ganadora al centro
if winning_turtle:
    winning_turtle.goto(0, 0)
    winning_turtle.color(winning_color)
    winning_turtle.shapesize(2)  # Aumentar el tamaño

screen.exitonclick()
