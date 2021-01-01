from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        for car_color in COLORS:
            print(car_color)
            self.penup()
            self.shape('square')
            self.color(car_color)
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.goto(self.xcor(), random.choice(range(-100, 100)))