import turtle


ALIGNEMENT = "center"
FONT = ("Arial", 16, "normal")
HIGHSCORE_FILE = "data.txt"


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
        self.high_score = self.read_highscore()
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
            self.write_highscore()
        self.score = 0
        self.update()

    def read_highscore(self):
        """Read the old highscore from the data file."""
        try:  # To read the file with the high scores.
            with open(file=HIGHSCORE_FILE, mode="r") as file_handle:
                contents = file_handle.read()
                # Try to convert the file content into an integer.
                # Return 0 if someting other than digits is in the file.
                try:
                    high_score = int(contents)
                    return high_score
                except ValueError:  
                    return 0  
        # Return 0 if no file with the name HIGHSCORE_FILE is found.
        except FileNotFoundError:
            return 0

    def write_highscore(self):
        """Write the new high score to the data file."""
        with open(file=HIGHSCORE_FILE, mode="w") as file_handle:
            file_handle.write(str(self.high_score))