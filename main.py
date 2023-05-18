import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def condition():
    if player.finish():
        car_manager.speed_up()
        score.level_up()
    elif car_manager.collide(player.pos()):
        score.game_over()
        return False
    return True


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()

score = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.walk, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.check_traffic()
    car_manager.drive()
    game_is_on = condition()
    screen.update()

screen.exitonclick()