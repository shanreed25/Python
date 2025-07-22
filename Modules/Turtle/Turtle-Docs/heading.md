# Heading
- heading refers to the pointing direction
- heading indicates the direction the turtle is currently facing, measured in degrees
- the turtle understands cardinal directions (north, south, east, west) based on its coordinate system and heading

# Get Heading
- you can get the current heading with `turtle.heading()`.
    - returns the current orientation of a turtle object


#  `turtle.setheading()`
- sets the turtle's absolute heading/orientation to a specific angle in degrees
- pass in the desired angle in degrees: `turtle.setheading(10)`
- the default heading is 0 degrees, pointing towards the positive x-axis (East)
- the folowing heading values correspond to cardinal directions 
  - 0 degrees: East (positive x-axis): `turtle.setheading(0)`
  - 90 degrees: North (positive y-axis): `turtle.setheading(90)`
  - 180 degrees: West (negative x-axis): `turtle.setheading(180)`
  - 270 degrees: South (negative y-axis): `turtle.setheading(270)`
- it does not matter what the turtle's current heading is; calling turtle.setheading(90) will always make the turtle point North


#  `turtle.setheading()` vs `turtle.left(angle)`
- `turtle.left(angle)`: turns the turtle left (counter-clockwise) by a specified angle, relative to its current heading
- calling turtle.left(90) will turn the turtle 90 degrees counter-clockwise from its current direction
  - if the turtle is currently facing East (0 degrees), calling turtle.left(90) will make it face North (90 degrees)
  - if it is already facing North, calling turtle.left(90) again will make it face West (180 degrees)
- `setheading()`: Sets the turtle's heading to a specific absolute direction
- `left()`: Rotates the turtle a certain amount counter-clockwise from its current heading. 
**You can remember the difference like this: setheading() is like giving the turtle a compass direction to face, while left() is like telling it to turn a certain amount from where it's currently looking.**





# 