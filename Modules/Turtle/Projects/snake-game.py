from turtle import Turtle, Screen
import time
# USING tracer(0)*******************************************************************************************
# Create Snake Body
# Move Snake
my_canvas = Screen()
my_canvas.setup(width=600, height=600)
my_canvas.bgcolor("black")
my_canvas.title("Snake Game")


# Part - 3**********************************************************************************************************
# Create Snake Body
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("purple")
    new_segment.goto(position)
    segments.append(new_segment)

my_canvas.update()
# Move Snake: Part - 1***********************************************************************************************************************************************************
snake_is_moving = True
while snake_is_moving:

#range: where to start(start) where to stop(stop) how to get to move from start to stop(step)
    # so if want a range of  1, 2, 3 it would be range(start=1, stop=3 step=1)
    # if want a range of  3, 2, 1 it would be range(start=3, stop=1 step=-1)
    # [(0, 0), (-20, 0), (-40, 0)], we want to start at index 2 and stop at 0 so its range(start=2, stop=0 step=-1)
    # the range() function is not pure python, it comes from the C language, so it will not let us
    # use the parameter names and we will get: TypeError: range() takes no keyword arguments
    # for seg_num in range(2, 0, -1):
    # hard coded start(2) removed so if the number of segments change then the code will still work
    for seg_num in range(len(segments) - 1, 0, -1):
        # MOVE THE 3RD SEGMENT TO THE POSITION OF THE 2ND SEGMENT************************************************
        # when the loop starts, seg_num will be 2, which is the last segments position coordinates

        # we need to get the 2nd segment's position so we can move the 3rd segment to that position
        new_x = segments[seg_num -1].xcor() # 2nd segments x coordinate
        new_y = segments[seg_num - 1].ycor()# 2nd segments y coordinate

        segments[seg_num].goto(new_x, new_y)# the 3rd segment needs to go to the 2nd segment's coordinates
    segments[0].forward(20)
    segments[0].left(90)

my_canvas.exitonclick()