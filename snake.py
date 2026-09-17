"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import choice, randrange, sample
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista de 5 colores permitidos
# El rojo se reserva para indicar que el jugador perdió
colors = ['black', 'blue', 'green', 'purple', 'orange']

# Selecciona dos colores diferentes:
# uno para la serpiente y otro para la comida
snake_color, food_color = sample(colors, 2)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    """Move food randomly one step without leaving the window."""
    directions = [
        vector(10, 0),
        vector(-10, 0),
        vector(0, 10),
        vector(0, -10),
    ]

    direction = choice(directions)
    next_food = food.copy()
    next_food.move(direction)

    if inside(next_food):
        food.x = next_food.x
        food.y = next_food.y


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

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

    # Mover la comida aleatoriamente
    move_food()

    clear()

    # Dibujar serpiente con color aleatorio
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Dibujar comida con un color diferente
    square(food.x, food.y, 9, food_color)

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