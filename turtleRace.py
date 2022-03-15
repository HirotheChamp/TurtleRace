import turtle
import time
import random

from sympy import Q

WIDTH, HEIGHT = 500, 500 #width and height in call CAPS because they are constant values
COLORS = ['red', 'green', 'blue', 'orange', 'purple', 'black', 'brown', 'cyan', 'yellow', 'pink']

def get_number_of_racers():
    racers = 0
    while True:  # using while loop until a valid amount is implemented
        racers = input('Enter the Number of Racers (2-10): ')
        if racers.isdigit(): # can call isdigit() on strings
            racers = int(racers)
        else:
            print('Input is not numeric. Try Again!')
            continue

        if 2 <= racers <= 10: # if racers are between these two values then return racers
            return racers
        else:
            print('Number not in range 2-10. Try Again!')

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20) # every time i decide to move the turtle, it will randomly decide between 1 and 20
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT //2 - 10:
                return colors[turtles.index(racer)] # need to find winning turtle color


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color) # color in parenthese is the string that is already defined
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20) # set turtle's position
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Race!')

racers = get_number_of_racers()
init_turtle() #initialize turtle screen after getting the number of racers

random.shuffle(COLORS)
colors = COLORS[:racers] #gives us the first racers item from the list

winner = race(colors)
print(winner)

# racer = turtle.Turtle()

# racer.speed(1)
# racer.penup()
# racer.shape('turtle')
# racer.color('red')
# racer.forward(100)
# racer.left(90)
# racer.pendown()
# racer.right(100)
# racer.backward(90)


# racer2 = turtle.Turtle()
# racer2.speed(5)
# racer2.penup()
# racer2.shape('turtle')
# racer2.color('blue')
# racer2.forward(100)
# racer2.left(90)
# racer2.pendown()
# racer2.right(100)
# racer2.backward(90)
