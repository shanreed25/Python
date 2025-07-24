# Turtle Object 

# Initialize New Turtle
- `my_turtle = Turtle()`
  - has a shape attribute that has a default value of "arrow
- you can give the class a shape argumentto change the default shape
  - `my_turtle = Turtle(shape="turtle)`

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



# Turtle event Listeners
In Python's Turtle graphics module, the clear() method is a function of a Turtle object. It is used to delete the specific turtle's drawings from the screen without affecting its position or state, and without affecting drawings made by other turtles.

The home() function in Python's Turtle graphics module is used to move the turtle to its initial position and orientation.
Specifically, turtle.home() performs the following actions:
Moves to Origin:
It moves the turtle to the coordinates (0,0), which is the center of the drawing screen by default.
Resets Heading:
It sets the turtle's heading (direction it is facing) back to its default orientation, which is typically facing East (0 degrees).
This function is a convenient way to quickly reset the turtle's position and direction, often used at the beginning of a new drawing segment or to return to a known starting point.