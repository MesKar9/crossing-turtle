import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

odd_even = 0
game_is_on = True
while game_is_on:
    if odd_even % 4 == 0:
        car_manager.car_generator()
    odd_even += 1

    # Car collision
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # top wall collision
    if player.finish_line():
        car_manager.car_level_inc()
        scoreboard.level_inc()
    car_manager.car_move()
    screen.onkey(player.move, 'Up')
    time.sleep(0.1)
    screen.update()










screen.exitonclick()