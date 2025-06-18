from turtle import Turtle,Screen

screen = Screen()
tim = Turtle()
#after it starts listening, we have to bind a function that will be triggered when a particular key is pressed on keyboard.
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.home()
    tim.pendown()
#in order to listen to the events, we have to get hold of the screen object nd tell it to start listening
screen.listen()

#by this method we mean that,to listen for when the space bar is pressed nd only when that happens to trigger this
#move_forward function.(This function is used to bind fun to the key-release event of the key. In order to be able to
# register key-events, TurtleScreen must have focus.)
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()
#higher order function - when one function is put inside another function