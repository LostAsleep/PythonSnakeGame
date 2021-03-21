import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def main():
    """The main function of the snake game."""

    screen = turtle.Screen()             # First create the game screen.
    screen.setup(width=600, height=600)  # With it's dimensions.
    screen.bgcolor("black")              # Set the background color.
    screen.title("A Snake Game")
    screen.tracer(0)  # No automatic refreshing of the stuff on screen.

    snake = Snake()  # Create the snake using the Snake class.
    food = Food()    # Create the initial snake food.
    scoreboard = Scoreboard()

    screen.listen()  # Start listening for user input of specific keys.
    screen.onkey(snake.up, "Up")        # Remember: func without parens
    screen.onkey(snake.down, "Down")    # Remember: func without parens
    screen.onkey(snake.left, "Left")    # Remember: func without parens
    screen.onkey(snake.right, "Right")  # Remember: func without parens

    game_is_on = True
    while game_is_on:    # The main game loop.
        scoreboard.show_score()
        
        screen.update()  # Refresh the contents on screen.
        time.sleep(0.1)  # The speed of the game.
        snake.move()     # For continuous movement of the snake.

        if snake.head.distance(food) < 15:  # Detect collision with food.
            scoreboard.increase_score()
            food.refresh()  # Move food to another random location.

    screen.exitonclick()  # The window doesn't just disappear after looping.


if __name__ == "__main__":
    main()
