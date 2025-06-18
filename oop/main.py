#here we are going to create an object from a blueprint(class) that somebody else has already created
#and the blueprint(class) lives in another module called turtle.

#import turtle
#we have imported a module called turtle nd we fetched something from the module, in this case it is the Turtle() class
#t = turtle.Turtle()

#instead of writing all this i can just write

from turtle import Turtle, Screen

t = Turtle() # from turtle module we are taking a Turtle() class and t = new object created from the turtle class and its constructed. 
print(t)
t.shape("turtle")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.color("coral")
t.forward(100)
# car.speed - tells us that get the speed (attribute) from the car object. 
#the Screen rep the window in which the turtle module is going to show up.

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()