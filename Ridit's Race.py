from turtle import *
from random import * 
import turtle
import time

# Screen Setup
setup(800, 500)# width,height
title("Ridits Race")
bgcolor("blue")
speed(100)

# Heading
penup()
goto(-80, 205)
color("white")
write("Ridits Race", font = ("Arial", 25, "bold"))

#Dirt
goto(-350, 200)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

#Finish Line
gap_size = 20
shape("square")
penup()

#White square row 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()
#White square row 2
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

#Black square row 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

#Black square row 2
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()

#Creating the player
player_color = input("What is the color of your racer: ")
player_shape = input("What shape is your racer, Here are the shapes => classic,arrow,turtle,circle,square,triangle: ")
player_speed = 5
player = Turtle()
player.penup()
player.color(player_color)
player.shape(player_shape)
player.goto(-300, -150)
player.pendown()

#Pink Turtle
pink = Turtle()
pink.penup()
pink.color("pink")
pink.shape("turtle")
pink.goto(-300, 150)
pink.pendown()

#Green Turtle
green = Turtle()
green.penup()
green.color("green")
green.shape("turtle")
green.goto(-300, -50)
green.pendown()

#Yellow Turtle
yellow = Turtle()
yellow.penup()
yellow.color("yellow")
yellow.shape("turtle")
yellow.goto(-300, 50)
yellow.pendown()

#Creating the player speed
def speed(v):
    v += 1

time.sleep(1)

while (player.xcor() <= 230) and (pink.xcor() <= 230) and (green.xcor() <= 230) and (yellow.xcor() <= 230):
    turtle.listen()
    turtle.onkeypress(speed(player_speed), "d")
    player.forward(player_speed)
    pink.forward(randint(1, 10))
    yellow.forward(randint(1, 10))
    green.forward(randint(1, 10))
    if player.xcor() >= 230:
        player.shapesize(2.5)
        player.right(360)
        penup()
        color(player_color)
        goto(80, 200)
        write("You Win!!!", font = ("Monospace", 20, "bold"))
        hideturtle()
        break
    if pink.xcor() >= 230:
        pink.shapesize(2.5)
        pink.right(360)
        penup()
        color("pink")
        goto(80, -200)
        write("Pink Turtle Wins!!!", font = ("Monospace", 20, "bold"))
        hideturtle()
        break
    if yellow.xcor() >= 230:
        yellow.shapesize(2.5)
        yellow.right(360)
        penup()
        color("yellow")
        goto(80, -200)
        write("Yellow Turtle Wins!!!", font = ("Monospace", 20, "bold"))
        hideturtle()
        break
    if green.xcor() >= 230:
        green.shapesize(2.5)
        green.right(360)
        penup()
        color("green")
        goto(80, -200)
        write("Green Turtle Wins!!!", font = ("Monospace", 20, "bold"))
        hideturtle()
        break
