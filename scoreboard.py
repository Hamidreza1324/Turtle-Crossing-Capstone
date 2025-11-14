"""
Scoreboard Module
Displays current level and handles game over message.
"""

from turtle import Turtle

FONT = ("Courier", 24, "normal")
CENTER = (0, 0)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-300, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Refresh the level display."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase level by 1 when player crosses the road."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display GAME OVER in the center of the screen."""
        self.goto(CENTER)
        self.write("GAME OVER", align="center", font=FONT)

