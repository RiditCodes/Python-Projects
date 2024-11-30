import turtle

tur = turtle.Turtle()
tur.speed(0)
tur.pensize(3)
degrees = 0

for i in range(0, 15):
    if i <= 4:
        tur.fillcolor("red")
    elif i > 4 and i <= 9:
        tur.fillcolor("orange")
    else:
        tur.fillcolor("gold")
    tur.penup()
    tur.goto(0,0)
    tur.pendown()
    tur.setheading(degrees)
    tur.begin_fill()
    tur.circle(150,70)
    tur.left(110)
    tur.circle(150,70)
    tur.end_fill()
    degrees += 15

tur.fillcolor("yellow")
tur.setheading(0)
tur.penup()
tur.goto(0,0)
tur.pendown()

tur.begin_fill()
tur.circle(50)
tur.penup()
tur.goto(0,100)
tur.pendown()
tur.circle(30)
tur.end_fill()

tur.pensize(5)

tur.penup()
tur.goto(7,130)
tur.pendown()
tur.circle(1)

tur.penup()
tur.goto(-7,130)
tur.pendown()
tur.circle(1)

tur.penup()
tur.goto(10,0)
tur.pendown()
tur.right(90)
tur.forward(50)
tur.backward(10)
tur.left(70)
tur.forward(10)
tur.backward(10)
tur.right(140)
tur.forward(10)

tur.penup()
tur.goto(-10,0)
tur.pendown()
tur.setheading(-90)
tur.forward(50)
tur.backward(10)
tur.left(70)
tur.forward(10)
tur.backward(10)
tur.right(140)
tur.forward(10)

#hat

tur.fillcolor("black")
tur.penup()
tur.goto(-5,160)
tur.pendown()
tur.setheading(0)
tur.begin_fill()
tur.forward(50)
tur.left(90)
tur.forward(5)
tur.left(90)
tur.forward(20)
tur.right(90)
tur.forward(30)
tur.left(90)
tur.forward(50)
tur.left(90)
tur.forward(30)
tur.right(90)
tur.forward(20)
tur.left(90)
tur.forward(5)
tur.left(90)
tur.forward(50)
tur.end_fill()

tur.hideturtle()

turtle.done()