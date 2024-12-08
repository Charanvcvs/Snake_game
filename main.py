from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()


def toggle_pause():
    global is_pause
    is_pause = not is_pause


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(toggle_pause, "space")

game_is_on = True
is_pause = False
def game_loop():
    if not is_pause:
        screen.update()
        snake.move()

        # Detecting the food
        if snake.head.distance(food) < 20:
            food.refresh()
            snake.extend()
            score_board.add_score()

        # Detect collision with wall
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
            score_board.game_over()
            return  # End game loop if collision occurs

    # Continue game loop after 100 ms
    screen.ontimer(game_loop, 100)
game_loop()
screen.exitonclick()