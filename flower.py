import turtle

list1 = ["blue", "yellow", "black", "green", "red"]
tur = turtle.Turtle()
tur.speed(0)
for i in list1:
    tur.color(i)
    for x in range(0, 120):
        tur.forward(3)
        tur.right(3)
    for y in range(0, 120):
        tur.forward(6)
        tur.right(3)
    tur.left(70)
