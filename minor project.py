import turtle
import random

def draw_spiral():
    window=turtle.Screen()
    window.bgcolor("BLACK")
    rob=turtle.Turtle()
    rob.speed(10)
    rob.shape("classic")

    x=45
    for i in range(1,300):

        R=random.randrange(0,255)
        B=random.randrange(0,255)
        G=random.randrange(0,255)

        turtle.colormode(255)

        rob.color(R,B,G)
        rob.forward(x)
        rob.right(91)
        x=x+1

    window.exitonclick()

draw_spiral()
