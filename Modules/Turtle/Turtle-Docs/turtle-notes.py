from turtle import Turtle, Screen

my_canvas = Screen()
listening_turtle = Turtle()

# To start listening to events you have to tell the screen to listen
my_canvas.listen()

# Once you have the screen listening, you have to bind a function that
# will trigger when a particular key is pressed on the keyboard


# def move_forward():
#     listening_turtle.forward(20)
# Bind a key stroke to an event
# onkey() is a higher order function
# Parameters: function(no arguments) , key(string)
# when passing a function as an argument you do not add the parenthesis()
#"space" is the space bar
#my_canvas.onkey(fun=move_forward, key="space")# listen for when the space bar is pressed and then run the move_forward function
my_canvas.setup(width=500, height=400)
listening_turtle.penup()
listening_turtle.setx(x=-230)
listening_turtle.pendown()
listening_turtle.forward(472)
print(listening_turtle.xcor())
my_canvas.exitonclick()