# turtle.write()

- used to display text on the TurtleScreen at the turtle's current position
- turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
Functionality:
The turtle.write() method provides a way to add labels, instructions, or dynamic values to your Turtle graphics output. The text is written with the turtle's current position as the baseline for the text. You can customize the appearance and alignment of the text using the font and align parameters. The move parameter controls whether the turtle's position updates after the text is written

## Parameters
- **arg:** text or value to be written on the screen. This can be a string, number, or any object that can be converted to a string.
- **move:** a boolean value (True or False). If True, the turtle moves to the end of the written text. If False (default), the turtle remains at its original position after writing.
- **align:** specifies the text alignment relative to the turtle's position. Possible values are 'left' (default), 'center', or 'right'.
- **font:** a tuple specifying the font style. It consists of three elements:
    - **fontname:** name of the font (e.g., 'Arial', 'Courier', 'Times New Roman').
    - **fontsize:** size of the font in pixels.
    - **fonttype:** style of the font (e.g., 'normal', 'bold', 'italic'). 