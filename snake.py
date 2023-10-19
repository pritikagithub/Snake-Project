from turtle import Turtle
import time

#constants
SNAKE_SPEED = 0.1
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:

    def __init__(self):
        self.snake_speed = SNAKE_SPEED
        self.snake = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        x, y = 0, 0

        for i in range(3):
            new_snake_body = Turtle(shape="square")
            new_snake_body.color("white")
            new_snake_body.penup()
            new_snake_body.goto(x=x, y=y)
            x -= 20
            self.snake.append(new_snake_body)
        self.head = self.snake[0]
        self.head.color("red")

    def extend_snake(self):
        new_snake_body = Turtle(shape="square")
        new_snake_body.color("white")
        new_snake_body.penup()
        new_snake_body.goto(self.snake[-1].position())
        self.snake.append(new_snake_body)

    def move(self):
        for body in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[body - 1].xcor()
            new_y = self.snake[body - 1].ycor()
            self.snake[body].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)