import turtle
from itertools import cycle
import random

colors = cycle(["red", "orange", "yellow", "green", "blue", "purple"])

def draw_shape(size, angle, shift, shape):
    turtle.pencolor(next(colors))
    next_shape = ""
    if shape == "circle":
        turtle.circle(size)
        next_shape = "square" 
    elif shape == "square":
        for i in range(4):
            turtle.forward(size*2)
            turtle.left(90)
        next_shape = "circle"
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size + 5, angle + 10, shift + 1, next_shape)

turtle.bgcolor("black")
turtle.speed("fast")
turtle.pensize(4)
turtle.hideturtle()
draw_shape(30, 0, 1, "circle")