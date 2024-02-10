import turtle
tur = turtle.Screen()
tur.bgcolor("black")
tur.title("Here is a Mega Circle Pattern")

list1 = ["green", "cyan", "blue", "red", "orange", "yellow"]
turt = turtle.Turtle()
turt.hideturtle()
turt.speed(100)
turt.pensize(100)
for a in range(0, 3):
    for b in list1:
        turt.color(b)
        turt.circle(100)
        turt.left(20)
