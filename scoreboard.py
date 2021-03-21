import turtle


class Scoreboard(turtle.Turtle):
    """For displaying the current game score."""
    def __init__(self):
        """Initialize the scoreboard at the upper center of the game."""
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0

    def show_score(self):
        """Print the current score. Clear text before updating"""
        current_score = f"Score: {self.score}"
        self.goto(0, 280)
        self.clear()  # So that we get no overlaping text.
        self.write(arg=current_score, move=False, align="center")

    def increase_score(self):
        """Increases the score by one if called."""
        self.score += 1
