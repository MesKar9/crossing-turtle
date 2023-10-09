from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 1
        
    def car_generator(self):
        starting_y = randint(-280, 280)
        new_car = Turtle()
        new_car.shape('square')
        new_car.color(choice(COLORS))
        new_car.shapesize(stretch_len=2.0, stretch_wid=1.0)
        new_car.penup()
        new_car.setheading(180)
        new_car.setpos(300, starting_y)
        self.cars.append(new_car)
    
    def car_move(self):
        for i in range(len(self.cars)):
            car = self.cars[i]
            car.forward(self.level * STARTING_MOVE_DISTANCE)

    def car_level_inc(self):
        self.level += 1
