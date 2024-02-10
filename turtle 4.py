import turtle

tur = turtle.Turtle()
tur.screen.bgcolor("light green")
tur.pencolor("red")
tur.pensize(6)
tur.fillcolor("blue")
tur.speed(1)

tur.begin_fill()
for i in range(0, 6):
    tur.forward(100)
    tur.left(60)
tur.end_fill()

turtle.done()