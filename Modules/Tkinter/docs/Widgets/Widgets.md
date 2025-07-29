# Widgets
- components commonly referred to as widgets, are the fundamental building blocks used to construct Graphical User Interfaces (GUIs) in Python
- to get a widget to display we must specify how the widget is going to be displayed before it will show on the screen
    - you can do this by using [Layout Managers](./LayoutManagement.md)
- widgets are instances of specific classes within the Tkinter module and represent various interactive and display elements of an application

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
- **Toplevel:** Creates a new, independent window, often used for dialog boxes or secondary windows


# Widget Methods
- [`after()`]()
    - a universal widget method used to schedule a function to be called after a specified delay