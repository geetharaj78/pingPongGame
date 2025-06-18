from turtle import Turtle, Screen
import time
s = Screen()
s.setup(width = 600, height = 600)
s.bgcolor("black")
s.title("Retro Reptile")
start_pos = [(0,0),(-20,0),(-40,0)]

snakes = []
for position in start_pos:
    new_snakes = Turtle("square") #the turtle will get created in the centre pos
    new_snakes.color("green")
    new_snakes.penup()
    new_snakes.goto(position) #it will move to whatever pos we tell it to go to
    snakes.append(new_snakes)



game_is_on = True
while game_is_on:
    s.update() #we will update the screens once all the segments have move forward.
    time.sleep(0.1) #it will give a one sec delay for each seg moves.
    for snake in snakes:
        snake.forward(10)
s.exitonclick()