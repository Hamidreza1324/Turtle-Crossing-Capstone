"""
Car Manager Module
Handles creation, movement, and speed of cars in the Turtle Crossing Game.
"""

from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly create a car at a random y-position."""
        if randint(1, 6) == 1:  # ~1/6 chance to create a car each frame
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars to the left by current speed."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase speed of all cars when player completes a level."""
        self.car_speed += MOVE_INCREMENT

