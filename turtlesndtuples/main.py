from turtle import Turtle, Screen
#keyword, module name, keyword, thing in module
#from turtle module import turtle class

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
#drawing a square.
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)


#for the window to stay until we press something.
screen = Screen()
screen.exitonclick()