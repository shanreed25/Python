# `turtle.shape()`
- used to set or retrieve the shape of a turtle object
- call shape() without any arguments, it will return the name of the current shape of the turtle
    - `turtle.shape()`
- you can set the shape to one of the predefined shapes by passing its name as a string argument to the shape() method
    - `turtle.shape("turtle)`
- you can pass in the shape as a argument to the Turtle object when creating the turtle
    - `my_turtle = Turtle("circle")`

- `turtle.hideturtle()` makes the turtle icon disappear
    - does not remove the drawings made by that turtle

# Size


## Custom Shapes
- register custom shapes using `turtle.register_shape()`
- can be polygons or images
- once registered, these custom shapes can also be assigned to a turtle using turtle.shape()

# `turtle.shape.size`
- used to control the size and outline of the turtle's shape
- allows you to stretch the turtle's shape
    - perpendicular to its orientation (width)
    - in the direction of its orientation (length)
- allow you to set the width of its outline
- all turtle shapes start off as 20px x 20px
- `turtle_object.shapesize(stretch_wid=None, stretch_len=None, outline=None)`
- `turtle.shapesize(stretch_wid=5, stretch_len=1)`: width = 20 and height=100
    - because 20 X 5 = 100



# Parameters:
- **stretch_wid (optional):** A number (integer or float) representing the stretch factor perpendicular to the turtle's orientation (its "width"). Default is 1.
- **stretch_len (optional):** A number (integer or float) representing the stretch factor in the direction of the turtle's orientation (its "length"). Default is 1.
- **outline (optional):** An integer representing the width of the shape's outline. Default is 1.

- To increase the size proportionally: Provide the same value for stretch_wid and stretch_len
    `        my_turtle.shapesize(2, 2)  # Doubles the width and length`