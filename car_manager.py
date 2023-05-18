from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE
        self.spawn_rate = 0.1

    def spawn(self):
        y_cor = random.randint(-280, 280)
        car = Turtle()
        car.penup()
        car.goto(350, y_cor)
        car.shape("square")
        car.color(random.choice(COLORS))
        car.turtlesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        self.car_list.append(car)

    def drive(self):
        for car in self.car_list:
            car.forward(self.speed)
            if car.xcor() < -350:
                self.car_list.remove(car)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
        self.spawn_rate += 0.1

    def check_traffic(self):
        if random.random() < self.spawn_rate:
            self.spawn()

    def collide(self, player_pos):
        for car in self.car_list:
            if car.distance(player_pos) < 20:
                return True
        return False
