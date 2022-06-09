from turtle import Turtle, Screen

from food import Food
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nicholas` Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

speed = 0.07
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_points()
        # increasing teh difficulty
        speed -= 0.001

    # Detect collisions with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    # Detect collisions with tail.
    for part in snake.snake_parts[1::]:
        if snake.head.distance(part) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
