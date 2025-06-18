from turtle import Turtle
import random

t = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSlateGray", "SlateGray", "Wheat", "SeaGreen"]

directions = [0, 90, 180, 270]
t.pensize(15)
t.speed("fastest")

for _ in range(200):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(directions))
