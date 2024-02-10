import turtle

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(100, 100)
t.pendown()
t.color("blue")
t.begin_fill()
for i in range(1, 400):
    t.forward(2)
    t.right(1)
t.end_fill()

t.penup()
t.goto(130, 30)
t.pendown()
t.color("yellow")
t.begin_fill()
for i in range(1, 400):
    t.forward(1)
    t.right(1)
t.end_fill()
