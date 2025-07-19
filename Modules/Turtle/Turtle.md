# Turtle Module
- provides a "turtle" object that acts as a drawing pen, moving and drawing on a canvas

# Canvas
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
  - `screen.onkeypress(), screen.onclick(), screen.exitonclick()`: Managing events like key presses and clicks 
  - `screen.tracer(), screen.update()`: Controlling animation updates


# Cartesian coordinate system
- the drawing area operates on a Cartesian coordinate system with an X and Y axis
  - Origin (0,0):
  - the center of the Turtle Graphics window is the origin
  - where both the X and Y coordinates are zero
## X-axis
- the horizontal axis.
- positive X values extend to the right of the origin.
- negative X values extend to the left of the origin.

## Y-axis
- the vertical axis.
- positive Y values extend upwards from the origin.
- negative Y values extend downwards from the origin.

## Controlling Turtle Position using X and Y Coordinates
- functions that allow you to move the turtle to a specific absolute position on the screen
  - `turtle.goto(x, y)`:
    - provide it with its desired X and Y coordinates
  - `turtle.setx(x)`:
    - provide it a X coordinate
  - `turtle.sety(y)`:
    - provide it a Y coordinate
  - turtle.setheading(angle):
  - sets the turtle's orientation
    - 0 degrees is typically to the right (positive X-axis)
    - 90 degrees is up (positive Y-axis), and so on

## Retrieving Turtle's X and Y Coordinates:
- `turtle.xcor()`: 
  - Returns the current X-coordinate of the turtle.
- `turtle.ycor()`: 
  - Returns the current Y-coordinate of the turtle.
- `turtle.pos()`or `turtle.position()`:
  - Returns a Vec2D object (a tuple-like object) representing the turtle's current (x, y) coordinates.

  
# Pointing Direction: heading()
- heading refers to the pointing direction
- the `heading()` method gives the current orientation of a turtle object
- get the turtle's heading: `turtle.heading()`
  - set the turtle's heading: `turtle.setheading()`
  - changes the turtle's orientation
  - pass in the desired angle in degrees: `turtle.setheading(10)`
- the default heading is 0 degrees, pointing towards the positive x-axis (East)
- the heading values correspond to cardinal directions 
  - 0 degrees: East (positive x-axis)
  - 90 degrees: North (positive y-axis)
  - 180 degrees: West (negative x-axis)
  - 270 degrees: South (negative y-axis)
  

# Colors
- the turtle module likes to work with color [tuples]()