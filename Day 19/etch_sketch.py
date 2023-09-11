import turtle


ventana = turtle.Screen()
ventana.title("Etch-A-Sketch")
ventana.bgcolor("white")


lapiz = turtle.Turtle()
lapiz.speed(0)


def adelante():
    lapiz.forward(10)


def atras():
    lapiz.backward(10)


def izquierda():
    new_heading = lapiz.heading() + 10
    lapiz.setheading(new_heading)


def derecha():
    new_heading = lapiz.heading() - 10
    lapiz.setheading(new_heading)


def borrar():
    lapiz.clear()
    lapiz.penup()
    lapiz.home()
    lapiz.pendown()


ventana.listen()
ventana.onkey(adelante, "Up")
ventana.onkey(atras, "Down")
ventana.onkey(izquierda, "Left")
ventana.onkey(derecha, "Right")
ventana.onkey(borrar, "c")


ventana.onkey(ventana.bye, "q")


ventana.mainloop()
