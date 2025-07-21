# Heading
- heading refers to the pointing direction
- heading indicates the direction the turtle is currently facing, measured in degrees


# Get Heading
- you can get the current heading with `turtle.heading()`.
    - returns the current orientation of a turtle object


# Set Heading
- set the turtle's heading: `turtle.setheading()`
  - changes the turtle's orientation
  - pass in the desired angle in degrees: `turtle.setheading(10)`
- the default heading is 0 degrees, pointing towards the positive x-axis (East)
- the heading values correspond to cardinal directions 
  - 0 degrees: East (positive x-axis): `turtle.setheading(0)`
  - 90 degrees: North (positive y-axis): `turtle.setheading(90)`
  - 180 degrees: West (negative x-axis): `turtle.setheading(180)`
  - 270 degrees: South (negative y-axis): `turtle.setheading(270)`