from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(snake.snake_speed)
    snake.move()
    
    # Collision with the food:
    if snake.head.distance(food) < 15:
        snake.snake_speed *= 0.99
        food.refresh()
        score.update_score()
        snake.extend_snake()

    # Collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        is_game_on = False
        score.game_over()

    # Collision with tail:
    for body in snake.snake:
        if snake.head == body:
            pass
        elif snake.head.distance(body) < 15:
            is_game_on = False
            score.game_over()

screen.exitonclick()