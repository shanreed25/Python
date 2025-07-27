# Compoenets(Widgets)
- components commonly referred to as widgets, are the fundamental building blocks used to construct Graphical User Interfaces (GUIs) in Python
- to get a components to display we must specify how the components are going to be displayed before it will show on the screen
- widgets are instances of specific classes within the tkinter module and represent various interactive and display elements of an application

# Common Tkinter Widgets
- **Label:** Used to display static text or images.
- **Button:** A clickable element that triggers an action when pressed.
- **Entry:** A single-line text input field for user input.
- **Text:** A multi-line text input and display area, suitable for larger amounts of text.
- **Frame:** A container widget used to group and organize other widgets within a window.
- **Canvas:** Provides a drawing area for creating custom graphics, shapes, lines, and images.
- **Checkbutton:** A checkbox widget allowing users to select or deselect an option.
- **Radiobutton:** Used to create radio button groups where only one option can be selected at a time.
- **Listbox:** Displays a list of items from which the user can select one or more.
- **Scrollbar:** Used to add scrolling functionality to widgets like Text and Listbox when content exceeds the viewable area.
- **Scale:** Allows users to select a numerical value within a defined range using a slider.
- **Spinbox:** A numerical input field with up and down arrows for incrementing or decrementing the value.
- **Menubutton:** A button that opens a dropdown menu when clicked.
- **Menu:** Used to create menu bars, dropdown menus, and context menus.
- **Toplevel:** Creates a new, independent window, often used for dialog boxes or secondary windows.

# How Tkinter Widgets Work
- **Instantiation:** created by instantiating their respective classes (e.g., tk.Button(), tk.Label()).
- **Configuration:** can be customized using various options (e.g., text, bg, width, command) to control their appearance and behavior.
- **Layout Management:** are positioned and sized within the GUI using layout managers like pack(), grid(), or place().
- **Event Handling:** can be configured to respond to user interactions (e.g., button clicks, key presses) by binding events to specific functions or methods.

**To get a Component to display we must specify how that component is going to be displayed before it will show on the screen**
# `pack()`
- the easiest way to display a component is to use the `pack()` method to pack component onto the screen
- `pack()`: will place the component in the center by default
    - `pack(side="left")` will place component on the left
- [Packer Docs](https://docs.python.org/3/library/tkinter.html#the-packer)


# How widget work
- Tkinter arbitrary keyword arguments for a lot of the Methods properties or initializing Components
    - arbitrary keyword arguments(**kwargs), are collected into a dictionary
    - You can learn more about arbitrary keyword arguments [here](../../../Functions/docs/CustomizedFunctions.md#unlimitedarbitrary-keyword-arguments--kwargs)
- we can set these options in a number of ways
    1. When the object is initialize
        - `my_Label = Label(text="I am a label", font=("Arial", 24, "bold"))`
    2. Like they are keys in a dictionary, then set the value, this can also update text
        - `my_label["text"] = "I am a label"`
        - `my_label["font"] = (text="I am a label", font=("Arial", 12, "bold")`
    3. Using the config() method, this can also update text
        - `my_label.config(text="I am a label", font=("Arial", 24, "bold"))`
