from turtle import Turtle

class Paddle(Turtle): #for the paddle class to inherit all the things from paddle class
#now our paddle class is the same as the turtle class.
    def __init__(self,position):
        super().__init__()
        # creating one paddle.
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.goto(position)

    def _up(self):
     new_y = self.ycor() + 20
     self.goto(self.xcor(), new_y)

    def _down(self):
     new_y = self.ycor() - 20
     self.goto(self.xcor(),new_y)

    def bounce(self):
        self.y_move *= -1




