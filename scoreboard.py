import turtle


ALIGNEMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(turtle.Turtle):
    """For displaying the current game score."""

    def __init__(self):
        """Initialize the scoreboard at the upper center of the game."""
        super().__init__()
        self.color("white")
        self.hideturtle()  # No need to actually see the Turtle.
        self.penup()       # No superfluous lines drawn.
        self.goto(0, 275)  # Upper center.
        self.score = 0
        self.high_score = 0
        self.update()      # Print the intial score.

    def update(self):
        """Print the current score. Clear text before updating"""
        scores = f"Score: {self.score} High Score: {self.high_score}"
        self.clear()  # So that we get no overlaping text.
        self.write(arg=scores, move=False, align=ALIGNEMENT, font=FONT)

    def increase_score(self):
        """Increases the score by one if called and updates the board."""
        self.score += 1
        self.update()

    def reset(self):
        """Update the high score if neccessary and reset score."""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    # def game_over(self):
    #     """Print the game over message."""
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(arg="GAME OVER", align=ALIGNEMENT, font=FONT)
