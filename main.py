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

    snake = Snake()   # Create the snake using the Snake class.
    food = Food()     # Create the initial snake food.
    scoreboard = Scoreboard()  # Create the scoreboard upper center.

    screen.listen()   # Start listening for user input of specific keys.
    screen.onkey(snake.up, "Up")        # Remember: func without parens.
    screen.onkey(snake.down, "Down")    # Remember: func without parens.
    screen.onkey(snake.left, "Left")    # Remember: func without parens.
    screen.onkey(snake.right, "Right")  # Remember: func without parens.

    game_is_on = True
    while game_is_on:    # The main game loop.
        screen.update()  # Refresh the contents on screen.
        time.sleep(0.1)  # The speed of the game.
        snake.move()     # For continuous movement of the snake.

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()     # Increase/Update score.
            food.refresh()  # Move food to a different random location.
            snake.extend()  # Add one segment to the snake body.

        # Detect collision with wall.
        out_of_x_bounds = snake.head.xcor() > 280 or snake.head.xcor() < -280
        out_of_y_bounds = snake.head.ycor() > 280 or snake.head.ycor() < -280
        if out_of_x_bounds or out_of_y_bounds:
            game_is_on = False

        # Detect collision with tail.
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                break

    scoreboard.game_over()  # Print game over at the center of the screen.
    screen.exitonclick()    # The window doesn't just disappear after looping.


if __name__ == "__main__":
    main()
