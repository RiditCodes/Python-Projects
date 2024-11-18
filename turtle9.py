import turtle

tur = turtle.Turtle()
tur.pensize(10)

tur.penup()
tur.goto(0, 0)
tur.pendown()

for i in range(3):
    tur.forward(150)
    tur.left(120)

turtle.done()