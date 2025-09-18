# Tkinter
- the standard graphical user interface (GUI) library that comes with Python installations
    - on Linux, Microsoft Windows, and macOS, meaning it generally does not require a separate installation if Python was installed with the Tk/Tcl and IDLE checkbox enabled
- a thin, object-oriented layer on top of the Tk toolkit, Tkinter is essentially a wrapper around Tk
    - Tkinter communicates with an embedded Tcl interpreter that, in turn, interacts with the underlying Tk library
    
______________________________________________________________________________________________________________________

## Tk and Tcl Integration
- TK is the foundation for Tkinter
- TK is a cross-platform GUI toolkit written in C and controlled by the Tcl (Tool Command Language) scripting language
- Tk provides the core functionality and widgets (like buttons, labels, text fields, etc.) for building graphical applications
### Platform Abstraction:
- Tk and, by extension, Tkinter, achieve cross-platform compatibility by utilizing the native GUI facilities of the operating system
- For example, on Windows, it uses GDI; on macOS, it uses Cocoa; and on Unix/X11, it uses Xlib
- This abstraction allows you to write a single Tkinter application that can run on different operating systems with a consistent appearance (especially with Ttk widgets)
- Because Tk is cross-platform, applications built with Tkinter in Python also benefit from this compatibility, allowing them to run on various operating systems like Windows, macOS, and Linux with a consistent appearance
___________________________________________________________________

## Widget Creation
- Tkinter provides Python classes that represent various GUI elements, known as widgets (Button, Label, Entry, Frame etc...)
- You create instances of these classes to build your application's interface
- [More](./docs/Widgets/Widgets.md)
___________________________________________________________________

## Layout Management
- After creating widgets, you need to arrange them within your window
- Tkinter offers three primary geometry managers:
- [More](./docs/LayoutManagement.md)
___________________________________________________________________


## Event Loop
- core of a Tkinter application is its event loop, initiated by calling the `mainloop()` method on the main window object
- This method continuously listens for user interactions (like button clicks, key presses, mouse movements) and system events
- [More](./docs/mainloop.md)
___________________________________________________________________

## Event Handling
- When an event occurs, Tkinter triggers associated callback functions or methods that you define
- These functions contain the logic to respond to the event, such as updating widget content, opening new windows, or performing calculations
___________________________________________________________________

# Importing Tkinter
- all components come from the `tkinter` class
- `import tkinter`
    - when importing like this we have to use `tkinter.Tk()` for every component/widget
    - use if you are going to just use a few components 
- `from tkinter import *`
    - when importing liked this using *(all) will import all classes and and constants  then we can use the widgets like this `TK()`
    - use if you are going to use alot of the components, this will help cut down on typing
_________________________________________________________________


- [Root Window](./docs/RootWindow.md)
- [Event Loop](./docs/EventLoop.md)
- [Widgets](./docs/Widgets/Widgets.md)
- [Layout Management](./docs/LayoutManagement.md)
- [Event Handling](./docs/EventHandling.md)