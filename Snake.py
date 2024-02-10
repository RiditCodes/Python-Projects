from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -340 < head.x < 330 and -280 < head.y < 280

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")
        update()
        return

    snake.append(head)

    if head == food:
        print("Snake:", len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, "green")

    square(food.x, food.y, 9, "red")
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), "d")
onkey(lambda: change(-10, 0), "a")
onkey(lambda: change(0, 10), "w")
onkey(lambda: change(0, -10), "s")
move()
done()
