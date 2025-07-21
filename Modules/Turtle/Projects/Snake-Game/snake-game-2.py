from turtle import Turtle, Screen
import time
my_canvas = Screen()
my_canvas.setup(width=600, height=600)
my_canvas.bgcolor("black")
my_canvas.title("Snake Game")
my_canvas.tracer(0)


starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("purple")
    new_segment.goto(position)
    segments.append(new_segment)

# this is causing the code below it not to work so we have to move it
# FIND OUT WHY LATER?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
# my_canvas.update()
# screen.update() might not execute as expected because screen.update() typically pauses the program
# to display the changes made to the turtle graphics window
# To ensure your code runs, you need to either call screen.mainloop() or turtle.done() at the end of your script,
# or strategically place screen.update() calls to avoid blocking the execution flow.




# Move Snake: Part - 1***********************************************************************************************************************************************************
# snake_is_moving = True
# while snake_is_moving:
#     for seg in segments:
#         seg.forward(20)
#         my_canvas.update()# updates the screen after each segment has moved
#         time.sleep(1)# used to slow down animation so we can see what happening
########################################################################################
# the first segment will move, then the screen will update, sleep for 1 sec
# then the second segment will move, then the screen will update, sleep for 1 sec
# then the 3rd segment will move, then the screen will update, sleep for 1 sec
# then it will repeat
# so we need to move the my_canvas.update() outside of the for loop

# Move Snake: Part - 2***********************************************************************************************************************************************************
snake_is_moving = True
while snake_is_moving:
    my_canvas.update()# updates the screen after each segment has moved
    time.sleep(0.1)# slows the down animation so we can see what happening
    for seg in segments:
        seg.forward(20)
        segments[0].left(90)
# so if we try to turn the snake head, the first segment will turn but, the second and third will keep moving forward
# this happens because the segments are not linked
###################################################################################################
# so instead of moving everything forwards, we can move the 3rd segment to move to the 2nd segment's position
# move the 2nd segment to the 1st segment position
# then get the first segment to make the move
# to do this we have to change the for loop
#****************************************************************************************************************



my_canvas.exitonclick()




