from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT  # Increase speed when player levels up

    def reset(self):
        """Resets the car manager state, including speed and clearing all cars."""
        # Hide and remove all cars
        for car in self.all_cars:
            car.hideturtle()  # Hide car turtle
        self.all_cars.clear()  # Clear the list of cars

        # Reset speed to initial value
        self.car_speed = STARTING_MOVE_DISTANCE  # Reset car speed to its initial value

    

