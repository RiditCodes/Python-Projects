import turtle

tur = turtle.Turtle()
tur.color("blue", "yellow")
tur.hideturtle()
def make_triangle(var):
    var.begin_fill()
    for i in range(0, 3):
        var.forward(100)
        var.left(120)
    var.end_fill()
make_triangle(tur)
