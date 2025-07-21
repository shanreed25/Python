from turtle import Screen
from snake import Snake
import time
# Control Snake
# Put Food on screen
# Detect collision with food
# Create Score Board
# Detect collision with wall
my_canvas = Screen()
my_canvas.setup(width=600, height=600)
my_canvas.bgcolor("black")
my_canvas.title("Snake Game")
my_canvas.tracer(0)

# Create Snake Body
my_snake = Snake()


# Move Snake
my_canvas.listen()
my_canvas.onkey(fun=my_snake.move_down, key="Down")
my_canvas.onkey(fun=my_snake.move_up,  key="Up")
my_canvas.onkey(fun=my_snake.move_left, key="Left")
my_canvas.onkey(fun=my_snake.move_right, key="Right")


snake_is_moving = True
while snake_is_moving:
    my_canvas.update()
    time.sleep(0.1)
    my_snake.move()

my_canvas.exitonclick()