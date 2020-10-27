"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

# A01701879 María José Díaz Sánchez
# A00829556 Santiago Gonzalez Irigoyen
#Este juego es una versión en python del juego de la serpiente

from turtle import *
from random import randrange
from freegames import square, vector
import random

'''Aquí se crean la comida y el cuerpo de la serpiente a través de vectores'''
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    #Esta función cambia la dirección de la serpiente
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."

    # Esta función regresa un booleano de verdadero y falso para ver si la cabeza de la serpiente esta dentro de los límites
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

        head = snake[-1].copy()#crea la variable cabeza
        head.move(aim)#mueve la cabeza dependiendo

    if not inside(head) or head in snake: #este if es para ver si la serpiente chocó consigo misma y por ende, el juego debe terminar

        square(head.x, head.y, 9, 'red')
        update()
        return


    snake.append(head)

    if head == food:
        print('Snake:', len(snake))#esto dice el tamaño de la serpiente cada qeu come
        food.x = randrange(-15, 15) * 10
        snake.append(head)#crea a la serpiente (cuerpo + cabeza)
    if head == food:#se verifica si la serpiente se comió la comida
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10#esto hace que la comida aparezca en un lugar random
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #list of possible colors and random generator
    color = ['black', 'purple', 'green', 'yellow', 'orange', 'pink', 'blue']
    #generate random index to randomly allocate color for the snake
    e = random.randint(0, 6)
    color1 = color[e]

    for body in snake:
        square(body.x, body.y, 9, color1)#construye el cuerpo de la serpiente que es negro

    #generate new index for the color of the food
    e = random.randint(0, 6)
    color1 = color[e]

    square(food.x, food.y, 9, color1)#construye la comida que es verde
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)#genera el espacio de juego
hideturtle()
tracer(False)
listen()
#estas funciones son para reconocer las teclas como una forma de mover a la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
