import colorsys
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255 )

def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color =  (r, g, b)
    return color

tim.speed("fastest")

def draw_sinograph(size_of_graph):
    for _ in range(int(360/size_of_graph)):
        tim.color(randomcolor())
        tim.circle(10)
        tim.setheading(tim.heading()+ size_of_graph)

draw_sinograph(5)

s = t.Screen()
s.exitonclick()


