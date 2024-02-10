import turtle

tur = turtle.Turtle()
tur.screen.bgcolor("blue")
tur.pensize(10)

tur.penup()
tur.goto(-100, 100)
tur.pendown()

for i in range(4):
    tur.forward(150)
    tur.left(90)
    print(i)

turtle.done()