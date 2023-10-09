from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEAD_ANGLE = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(HEAD_ANGLE)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
            return True
