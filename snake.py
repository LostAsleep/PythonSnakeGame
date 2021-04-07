import turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """The Snake class of the snake game.

    Contains the information of the snake body
    and the movement methods."""

    def __init__(self):
        """Create the initial 3 segments upon initialization."""
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

        STARTING_POSITIONS is a list of 3 tuples."""
        for pos in STARTING_POSITIONS:
            # Appending of each segment to the body is handled by the
            # create_snake_segment_function.
            self.create_snake_segment(pos[0], pos[1])

    def reset(self):
        """Clear the snake and create initialize a new one."""
        for segment in self.body:
            segment.hideturtle()
        self.body.clear()
        self.create_starting_snake()
        self.head = self.body[0]

    def extend(self):
        """Add one segment to the snake.

        The position of the new segment is the position of the last segment."""
        last_pos = self.body[-1].position()
        self.create_snake_segment(last_pos[0], last_pos[1])

    def move(self):
        """This moves the complete snake.

        The movement starts from the end of the 'tail' to prevent
        any gaps showing in the snake body. The last segment goes
        to the position of the second to last etc.

        And finally the head moves one standard movement forward."""

        for segment_num in range((len(self.body) - 1), 0, -1):
            new_x = self.body[segment_num - 1].xcor()
            new_y = self.body[segment_num - 1].ycor()
            self.body[segment_num].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        """Change the direction of the Snake head to up.

        Remember that the snake can't do 180 degree turns."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the direction of the Snake head to down.

        Remember that the snake can't do 180 degree turns."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the direction of the Snake head to left.

        Remember that the snake can't do 180 degree turns."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the direction of the Snake head to right.

        Remember that the snake can't do 180 degree turns."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
