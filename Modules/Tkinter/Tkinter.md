# Tkinter
- the standard Python interface to the Tk GUI toolkit
- preinstalled with python, and is the standard Graphical User Interface (GUI) library
- is included with standard Python installations on Linux, Microsoft Windows, and macOS, meaning it generally does not require a separate installation if Python was installed with the Tk/Tcl and IDLE checkbox enabled


# Root Window
- the root window is the main window of a Tkinter application, typically created using `Tk()`
    - `root = tkinter.Tk()`
- provides methods like pack(), grid(), and place() to control the arrangement and positioning of widgets within a window


# mainloop()
- `mainloop()` allow applications operate on an event loop
- this loop continuously monitors for user interactions (like button clicks or key presses) and updates the display accordingly
    - under the hood this loop looks something like

               while True:
                 listen
            
- keeps the window on screen and listening for screen events
- `root.mainloop()` nust be the last line of code