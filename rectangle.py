import turtle

start = turtle.Turtle()
start2 = turtle.Screen()
start2.title("Two Rectangles")
start.hideturtle()

start.color("#F907E7", "#0719F5")
start2.bgcolor("#F907E7")
start.begin_fill()
for i in range(0, 2):
    start.forward(200)
    start.right(90)
    start.forward(70)
    start.right(90)
start.end_fill()
start.penup()
start.left(90)
start.forward(100)
start.color("#2BFA06", "#FAF606")
start.right(90)
start.begin_fill()
for i in range(0, 2):
    start.forward(200)
    start.right(90)
    start.forward(70)
    start.right(90)
start.end_fill()
