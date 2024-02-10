import turtle

tur = turtle.Turtle()
tur.screen.bgcolor("light green")
tur.speed(0)

#head
tur.fillcolor("blue")
tur.begin_fill()
tur.circle(115)
tur.end_fill()

tur.fillcolor("white")
tur.begin_fill()
tur.circle(100)
tur.end_fill()

#red ribbon
tur.penup()
tur.goto(-70, 15)
tur.pendown()
tur.fillcolor("red")
tur.begin_fill()

for i in range(0, 2):
    tur.forward(140)
    tur.right(90)
    tur.forward(20)
    tur.right(90)

tur.end_fill()

#eye 1
tur.penup()
tur.goto(-40,175)
tur.pendown()
tur.fillcolor("white")
tur.begin_fill()
tur.circle(17.5)
tur.end_fill()

tur.fillcolor("black")
tur.begin_fill()
tur.circle(13)
tur.end_fill()

tur.fillcolor("white")
tur.begin_fill()
tur.circle(8)
tur.end_fill()

#eye 2
tur.penup()
tur.goto(40,175)
tur.pendown()
tur.fillcolor("white")
tur.begin_fill()
tur.circle(17.5)
tur.end_fill()

tur.fillcolor("black")
tur.begin_fill()
tur.circle(13)
tur.end_fill()

tur.fillcolor("white")
tur.begin_fill()
tur.circle(8)
tur.end_fill()

#nose
tur.penup()
tur.goto(0, 120)
tur.pendown()
tur.fillcolor("red")
tur.begin_fill()
tur.circle(17.5)
tur.end_fill()

tur.penup()
tur.goto(0, 130)
tur.pendown()
tur.fillcolor("white")
tur.pencolor("white")
tur.begin_fill()
tur.circle(3)
tur.end_fill()

tur.pencolor("black")

#mouth
tur.penup()
tur.goto(-60, 80)
tur.pendown()
tur.fillcolor("maroon")
tur.right(90)
tur.begin_fill()
tur.circle(60, 180)
tur.end_fill()

#line
tur.penup()
tur.goto(0, 80)
tur.pendown()
tur.forward(40)

tur.hideturtle()
turtle.mainloop()