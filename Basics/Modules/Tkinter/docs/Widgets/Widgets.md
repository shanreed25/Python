# Widgets
- are the fundamental building blocks used to construct Graphical User Interfaces (GUIs) in Python
- widgets are instances of specific classes within the Tkinter module
- each widget object represents a specific visual component in the graphical user interface
- widget methods are the tools you use to control and interact with those blocks, bringing your application to life
- to get a widget to display we must specify how the widget is going to be displayed before it will show on the screen
    - you can do this by using [Layout Managers](./LayoutManagement.md)


___________________________________________________________________________________________________________________________________

# Widget Methods
- widgets and widget methods are intrinsically linked through object-oriented programming principles
- because methods are functions that belong to a specific widget object, they allow you to configure appearance, control behavior, retrieve information and manage state
- [More](./methods/WidgetMethods.md)

___________________________________________________________________________________________________________________________________


# Using Widgets
1. **Instantiation** 
    - To use widgets a [root window](../RootWindow.md) object must be created using the `Tk()` class
    - Widgets are objects so they must be instantiated
        - Example: `my_label = Label()`
2. **Configuration**
    - customize using various options (text, bg, width, command, fg etc...) to control their appearance and behavior
3. **[Manage Layout](../LayoutManagement.md)**
    - position and size widgets within the GUI
4. **Handle Events**
    - if widget needs to respond to user interactions (button clicks, key presses), you will need to bind events to specific functions or methods that you create


___________________________________________________________________________________________________________________________________


# Commonly Used Widgets
- [`Label()`]() display static text or images
- [`Button()`]() clickable element that triggers an action when pressed
- [`Entry()`]() a single-line text input field for user input
- [`Text()`]() a multi-line text input and display area, suitable for larger amounts of text
- [`Frame()`]() a container widget used to group and organize other widgets within a window
- [`Canvas()`]() provides a drawing area for creating custom graphics, shapes, lines, and images
- [`Checkbutton()`]() a checkbox widget allowing users to select or deselect an option
- [`Radiobutton()`]() used to create radio button groups where only one option can be selected at a time
- [`Listbox()`]() displays a list of items from which the user can select one or more
- [`Scrollbar()`]() used to add scrolling functionality to widgets like Text and Listbox when content exceeds the viewable area
- [`Scale()`]() allows users to select a numerical value within a defined range using a slider
- [`Spinbox()`]() a numerical input field with up and down arrows for incrementing or decrementing the value
- [`Menubutton()`]() a button that opens a dropdown menu when clicked
- [`Menu()`]() used to create menu bars, dropdown menus, and context menus
- [`Toplevel()`]() creates a new, independent window, often used for dialog boxes or secondary windows
- [`PhotoImage()`]()