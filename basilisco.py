from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#color library
colors = ['pink','yellow','light blue','cyan','green']

#assign two different colors to the snake and the food
a = random.randint(0,4)
b = a
while a == b:
    b = random.randint(0,4)
color1 = colors[a]
color2 = colors[b]

#change direction by choosing heading coordinates
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    #20% probabilidad de que la comida se mueva
    c = random.randint(0, 3)
    if c == 2:
        #dirección de movimiento
        d = random.randint(0, 3)
        if d == 0:
            #movimiento una unidad a la derecha
            food.x = food.x + 10
        if d == 1:
            food.x = food.x - 10
        if d == 2:
            food.y = food.y + 10
        if d == 3:
            food.y = food.y - 10

#que hacer cuando se some a si misma
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

#como comer
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

#definir posición y color de la serpiente
    for body in snake:
        square(body.x, body.y, 9, color1)

#definir posición y color de la comida
    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
