import turtle

p = turtle.Turtle()
p.color("red")
def pentagon(var):
    var.begin_fill()
    for i in range(0, 5):
       var.forward(100)
       var.left(72)
    var.end_fill()
pentagon(p)
