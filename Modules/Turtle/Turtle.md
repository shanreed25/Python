# Turtle Module
- provides a "turtle" object that acts as a drawing pen, moving and drawing on a canvas to create graphics
- `turtle.Turtle()` is used to create a new "turtle" object
  - invokes the constructor of the Turtle class, creating a new instance of a Turtle object
    - allowing you to create multiple independent turtle objects
  - represents an on-screen "turtle" or pen 
  - comes with a set of methods that allow you to manipulate its position, orientation, appearance, and drawing behavior

# Turtle Object Attributes
- **Position:**
  - Represents the turtle's current location on the canvas, typically expressed as (x, y) coordinates in pixels. You can retrieve this with `turtle.position()` or `turtle.pos()`.
- **Heading:**
  - Indicates the direction the turtle is currently facing, measured in degrees. In standard mode, 0 degrees is east, 90 degrees is north, 180 degrees is west, and 270 degrees is south. You can get the current heading with `turtle.heading()`.
- **Color:**
  - Determines the color of the line drawn as the turtle moves and the color of the turtle's shape itself. This can be set using `turtle.color()`.
- **Pensize/Width:**
  - Controls the thickness of the line drawn by the turtle's pen. You can get or set this with `turtle.pensize()` or `turtle.width()`
- **Pendown/Penup state:**
  - A boolean attribute indicating whether the turtle's pen is currently "down" (drawing) or "up" (not drawing). This state is controlled by methods like `turtle.pendown()` and `turtle.penup()`.
- **Speed:**
  - Governs the animation speed of the turtle's movements. It's an integer from 0 (no animation, instant drawing) to 10 (fastest animation). You can set or retrieve it using `turtle.speed()`.
- **Shape:**
  - Defines the visual representation of the turtle, such as "arrow", "turtle", "circle", "square", "triangle", or "classic". This can be changed with `turtle.shape()`.
- **Fillcolor:**
  - Specifies the color used to fill shapes drawn with `begin_fill()` and `end_fill()`. This is set with turtle.fillcolor().


# Initialize New Turtle
- `my_turtle = Turtle()`
  - has a shape attribute that has a default value of "arrow
- you can give the class a shape argumentto change the default shape
  - `my_turtle = Turtle(shape="turtle)`





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

  

  

# Colors
- the turtle module likes to work with color [tuples]()




# Turtle event Listeners
In Python's Turtle graphics module, the clear() method is a function of a Turtle object. It is used to delete the specific turtle's drawings from the screen without affecting its position or state, and without affecting drawings made by other turtles.

The home() function in Python's Turtle graphics module is used to move the turtle to its initial position and orientation.
Specifically, turtle.home() performs the following actions:
Moves to Origin:
It moves the turtle to the coordinates (0,0), which is the center of the drawing screen by default.
Resets Heading:
It sets the turtle's heading (direction it is facing) back to its default orientation, which is typically facing East (0 degrees).
This function is a convenient way to quickly reset the turtle's position and direction, often used at the beginning of a new drawing segment or to return to a known starting point.


# Turtle screen.tracer()
- used to control the animation and updating of the drawing screen
- primary purpose is to optimize the drawing process, especially when dealing with complex or repetitive drawing operations
- `screen.tracer(0)` allows for efficient, controlled drawing by deferring screen updates
- `screen.update()` then explicitly renders the accumulated changes
- when you want something to happen, but you don't want it to be seen until it is completed
- Example: if you create an animation to draw a house 
  - but you don't want it to be seen on the screen until the house is finished drawing