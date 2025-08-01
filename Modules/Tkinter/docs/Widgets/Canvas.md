# Canvas
**A fundamental building block for creating custom graphical interfaces and visualizations in Tkinter**
- allow you to layer things one on top of the other
    - order of the items matters if you want one thing on top of the other
- provides a blank area within a Tkinter application where various graphical elements can be drawn and manipulated
- a highly versatile widget used for creating custom graphics, visualizations, and even entire user interfaces

- **Key features and capabilities of the Canvas widget include:**
- **Drawing Primitives:** supports drawing basic shapes such as lines, rectangles, ovals (including circles), arcs, and polygons
- **Image and Text Display:** images (bitmaps and PhotoImages) and text can be placed and rendered on the canvas
- **Embedding Widgets:** other Tkinter widgets, such as buttons or entry fields, can be embedded within the canvas using `create_window()`
- **Item Manipulation:** individual items drawn on the canvas can be moved, resized, and modified after creation
- **Event Handling:** events, such as mouse clicks or key presses, can be bound to the canvas as a whole or to specific items on the canvas, allowing for interactive applications.
- **Tags and IDs:** items on the canvas are assigned unique IDs and can also be grouped using tags, facilitating efficient manipulation of multiple items simultaneously.
- **Scrolling:** canvas content can be made scrollable, allowing for the display of content larger than the visible canvas area.
_________________________________________________________________________________________
- `Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)`

# Display a Image In the Canvas
- you can create an image on a Tkinter Canvas widget using a `PhotoImage()` object
- Example: `canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)`
    - setting the canvas to 200x224
        - because the image is a .png image that is 200x223
        - but we want to work with even numbers so the canvas is 200x224
    - `canvas.create_image()`: requires a x and y value, and a image
        - x and y positions: `x = 100 y = 112`
            - using half the canvas width and height will put the image in the center
        - image: the image parameter expects a instance of the `PhotoImage()` class
            - so we can not do this: image="image.png"
            - we need to use the `PhotoImage()` class to read through a file to get hold of a image, then pass it to the `canvas.create_image()`
                - `img = PhotoImage(file="my_img.png")`
        - `canvas.create_image(100, 112, image=img )`

# Draw text on a Canvas widget
- `canvas.create_text()`
- Parameters:
    - `x`: The x-coordinate of the text's anchor point.
    - `y`: The y-coordinate of the text's anchor point.
    - `: options`**: A dictionary of keyword arguments to customize the text's appearance and behavior. Common options include:
        - `text`: The string of text to display. Use \n for line breaks.
        - `fill`: The color of the text (e.g., 'red', '#FF0000').
        - `font`: A tuple or string specifying the font family, size, and style (e.g., ('Arial', 12, 'bold'), 'Times 10 italic').
        - `anchor`: Specifies how the text is aligned relative to the (x, y) coordinates. Common values include 'center' (default), 'n', 's', 'e', 'w', 'nw', 'ne', 'sw', 'se'.
        - `width`: The maximum width of the text in pixels. If the text exceeds this width, it will automatically wrap to multiple lines.
        - `justify`: How lines of text are justified within the specified width. Options are 'left', 'center', or 'right'.
        - `state`: Controls the text's visibility and responsiveness to events. Options are 'normal' (default), 'disabled', or 'hidden'.
        - `tags`: A string or tuple of strings to assign tags to the text item, allowing for easier manipulation or event binding.




# Changing a Canvas Elemnt
- to change most widget text we can use **`config()`** :`button.config(text="New Text)`
- for a canvas element we need to use **`itemconfig()`**: `canvas.itemconfig(elementToChange, whatToChange)`
- If you want to change the textof this element: `my_text = canvas.create_text(100, 130, text="Some Text")`
    - you would use: `canvas.itemconfig(my_textElement, text="New Text)`

