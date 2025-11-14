"""
Player Module
Defines the turtle controlled by the player.
"""

from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")  # Personal tweak: turtle color changed
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        """Move the player turtle up by a fixed distance."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def go_to_start(self):
        """Return the player to the starting position."""
        self.penup()
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if the player reached the finish line."""
        return self.ycor() > FINISH_LINE_Y

