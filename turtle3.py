import turtle

tur = turtle.Turtle()
tur.screen.bgcolor("light green")
tur.fillcolor("green")
tur.pencolor("green")

tur.penup()
tur.goto(-100, -100)
tur.pendown()

tur.begin_fill()
for i in range(0, 4):
    tur.forward(300)
    tur.left(90)
tur.end_fill()
    
turtle.done()