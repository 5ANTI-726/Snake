from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['pink','yellow','blue','black','purple']
col_s = random.randint(0,4)
color_s = colors[col_s]
col_f = random.randint(0,4)
color_f = colors[col_f]
while col_f == col_s:
    col_s = random.randint(0,4)
    color_s = colors[col_s]
    col_f = random.randint(0,4)
    color_f = colors[col_f]
    if col_s != col_f:
        break
    

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
    
    #20% probabilidad de que se mueva la comida en cualquier dirección una 'unidad'
    c = random.randint(0, 4)
    if c == 3:
        #generación de número que decidirá si se mueve arriba, abajo, etc.
        d = random.randint(0, 3)
        if d == 0:
            #aquí se mueve a la derecha
            food.x = food.x + 10
        if d == 1:
            food.x = food.x - 10
        if d == 2:
            food.y = food.x + 10
        if d == 3:
            food.y = food.x - 10

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_s)

    square(food.x, food.y, 9, color_f)
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
