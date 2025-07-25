# Screen()
- `turtle.Screen()`: a function that returns a singleton TurtleScreen object
  - provides the drawing area for the Turtle objects
  - all the drawing operations performed by turtles are displayed on this screen
- singleton means it returns an existing TurtleScreen object if one has already been created
  - or it creates a new one and then returns it
  - ensures that there is only ever one active screen for the turtle module
- this object represents the graphics window or canvas where the turtle drawings will appear
- Screen Configuration: allows for various configurations of the drawing window 
  - `screen.title()`: Setting the title of the window 
  - `screen.bgcolor()`: Changing the background color 
  - `screen.setup()`: Controlling the size and position of the window 
  - `screen.listen()`
  - `screen.onkeypress(), screen.onclick(), screen.exitonclick()`: Managing events like key presses and clicks 
  - `screen.tracer(), screen.update()`: Controlling animation updates
____________________________________________________________________________________

# TOC

- [Shapes]()
- [Coordinate system]()
- [Screen Events]()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()


# Keeping Screen Open

- `screen.exitonclick()`
- `screen.mainloop()`
  - way to keep the screen open, even if code has finished running

# Getting Responses From Users
- `screen.textinput()`
  - used to obtain string input from the user through a pop-up dialog window

# Turtle screen.tracer()
- used to control the animation and updating of the drawing screen
- primary purpose is to optimize the drawing process, especially when dealing with complex or repetitive drawing operations
- `screen.tracer(0)` allows for efficient, controlled drawing by deferring screen updates
- `screen.update()` then explicitly renders the accumulated changes
- when you want something to happen, but you don't want it to be seen until it is completed
- Example: if you create an animation to draw a house 
  - but you don't want it to be seen on the screen until the house is finished drawing