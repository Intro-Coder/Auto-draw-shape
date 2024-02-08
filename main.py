
from turtle import Turtle, Screen
from random import choice

pagong = Turtle()
screen = Screen()

def draw_shape(side, angle):

    color = ("red", "blue", "green", "orange")

    for x in range(side):

        pagong.pencolor(choice(color))
        pagong.forward(100)
        pagong.right(angle)

    print(side)

# -----------------------------------

sides = 4
angle = 360 / sides

while sides < 11:
    draw_shape(sides,angle)
    sides += 1
    angle = 360 / sides

screen.exitonclick()
