import turtle
import random


class Food(turtle.Turtle):
    """The snake food. Will be randomly placed on the screen upon init."""

    def __init__(self):
        """Initialize the food object to a random location."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.possible_coordinates = list(range(-280, 300, 20))
        random_x, random_y = self.get_grid_coordinates()
        self.goto(random_x, random_y)

    def refresh(self):
        """Move the food object to a random location."""
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        random_x, random_y = self.get_grid_coordinates()
        self.goto(random_x, random_y)

    def get_grid_coordinates(self):
        """To be able to place the food on a grid with the snake segments.
        Asuming the snake moves on an 'imaginary' grid of 20s."""
        new_x = random.choice(self.possible_coordinates)
        new_y = random.choice(self.possible_coordinates)
        return new_x, new_y
