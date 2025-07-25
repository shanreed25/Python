# `addshape()`
- a method of the TurtleScreen object
- an alias for `register_shape()`
- used to add a new shape to the list of available turtle shapes within the TurtleScreen
- allows you to use custom shapes for your turtles instead of the default arrow, circle, square, triangle, or classic shapes
- For image shapes, traditionally, only GIF files were supported. However, newer versions of Tkinter (which underlies Turtle) may support other formats like PNG
- To use images in formats other than GIF, you would typically need to convert them to GIF first
- After adding a shape with `addshape()`, you must then use `turtle.shape(name)` on a Turtle object to apply that custom shape to the turtle
```
screen = Screen()

image = "my_img.gif"
screen.addshape(image)# adds the image to the screen, and then it can be used by a turtle

my_turtle = Turtle()
my_turtle.shape(image)
```