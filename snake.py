import turtle
import time


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    """The Snake class of the snake game.

    Contains all position information of the snake body and most
    if not all movement methods."""


    def __init__(self):
        """Create the initial 3 segment snake body upon initialization."""
        self.body = []
        self.create_starting_snake()
        self.head = self.body[0]


    def create_snake_segment(self, x_pos, y_pos):
        """Initialize a snake segment as a turtle object."""
        segment = turtle.Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(x=x_pos, y=y_pos)
        self.body.append(segment)


    def create_starting_snake(self):
        """Create the initial snake with 3 snake segments.

        positions is a list of tuples."""
        for pos in STARTING_POSITIONS:
            # Appending of each segment to the body is handled by the
            # create_snake_segment_function.
            self.create_snake_segment(pos[0], pos[1])


    def move(self):
        """This moves the complete snake.

        The movement starts from the end of the 'tail' to prevent
        any gaps showing in the snake body. The last segment goes
        to the position of the second to last etc.

        And finally the head gets moved one standard movement forward."""

        for segment_num in range((len(self.body) - 1), 0, -1):
            new_x = self.body[segment_num - 1].xcor()
            new_y = self.body[segment_num - 1].ycor()
            self.body[segment_num].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)


    def up(self):
        """Change the direction of the Snake head to up."""
        self.head.setheading(90)


    def down(self):
        """Change the direction of the Snake head to down."""
        self.head.setheading(270)


    def left(self):
        """Change the direction of the Snake head to left."""
        self.head.setheading(180)


    def right(self):
        """Change the direction of the Snake head to right."""
        self.head.setheading(0)

