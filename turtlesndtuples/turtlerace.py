import turtle
from turtle import Turtle,Screen
import random
is_the_race_on = True
screen = Screen()
screen.setup(width= 500,height = 400)
bet = screen.textinput(title = "make your bet",prompt = "which turtle will win the race? enter a color: ")
colors = ["red","blue","green","yellow","purple","pink"]
y_positions = [-70,-40,-10,20,50,80]
all_the_turtles = []

for turt_index in range(0,6):
    new_turt = Turtle(shape ="turtle")
    new_turt.penup()
    new_turt.color(colors[turt_index])
    new_turt.goto(x = 230, y = y_positions[turt_index])
    all_the_turtles.append(new_turt)

if bet:
    is_the_race_on = True

while is_the_race_on:

    for turtle in all_the_turtles:
        if turtle.xcor() > 230:
            is_the_race_on = False
            win_color = turtle.pencolor()
            if win_color == bet:
                print(f"you've won the race! The {win_color} turtle is the winner!")
            else:
                print(f"you've won! the {win_color} turtle is the winner!")

    random_distance = random.randint(0,10)
    turtle.forward(random_distance)

screen.exitonclick()