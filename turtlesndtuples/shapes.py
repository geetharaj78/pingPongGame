from turtle import Turtle, Screen
import random

t = Turtle()

colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_n in range(3,11):
    t.color(random.choice(colors))
    draw_shape(shape_n)