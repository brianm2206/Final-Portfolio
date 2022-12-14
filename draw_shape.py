#Brian Molina
#11/10/10

# Asks questions about what shape and color and draws it.

length = input('Enter turtle length: ')
color = input('Enter turtle color: ')
shape = input('triangle or square: ')

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.pencolor(color)
if shape == 'square':
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)

else:
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.forward(length)