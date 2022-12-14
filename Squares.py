#Brian Molina
#11/25/2022

# Problem 5. produce an image shown.
import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

wn.exitonclick()