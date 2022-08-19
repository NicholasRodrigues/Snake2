from turtle import Screen, Turtle

from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time





# Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nicholas` Snake Game")
screen.tracer(8)

turtle = Turtle()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


def game_over():
    turtle.hideturtle()
    turtle.color("white")
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write("GAME OVER", False, "center", ("Courier", 24, "normal"))
    turtle.goto(0, -50)
    turtle.write(f"Your Final Score: {scoreboard.points}\nHigh Score: {scoreboard.high_score}", False, "center",
               ("Courier", 15, "italic"))
    time.sleep(3)
    turtle.clear()



screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

speed = 0.06
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
        game_over()
        time.sleep(3)
        scoreboard.reset()
        snake.reset()

    # Detect collisions with tail.
    for part in snake.snake_parts[1::]:
        if snake.head.distance(part) < 10:
            game_over()
            time.sleep(3)
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
