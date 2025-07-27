# Root Window
- the root window is the main window of a Tkinter application, typically created using `Tk()`
    - `root = tkinter.Tk()`
- provides methods like pack(), grid(), and place() to control the arrangement and positioning of widgets within a window
- the window is going to scale to include all components that you put inside

- **Add Custom Title:** `root.title("My TK Window")# Custom Title`
- **Window Size:**


# Compoenets
- to get a components to display we must specify how the components are going to be displayed before it will show on the screen

# `packer()`
- the easiest way to display a component is to use the `pack()` method to pack component onto the screen
- `pack()`: will place the component in the center by default
    - `pack(side="left")` will place component on the left
- [Packer Docs](https://docs.python.org/3/library/tkinter.html#the-packer)