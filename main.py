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

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.pause, "space")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#detecting the collision

    if snake.head.distance(food) < 20 :
        food.refresh()
        score_board.add_score()

#when food eats increase the snake segment and add to score every time we eat food

screen.exitonclick()