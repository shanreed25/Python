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