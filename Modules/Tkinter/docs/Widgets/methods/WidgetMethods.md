# Widget Methods
- widgets and widget methods are intrinsically linked through object-oriented programming principles
- because methods are functions that belong to a specific widget object, they allow you to configure appearance, control behavior, retrieve information and manage state

#### Widget Methods

- []()
- []()
- []()
- [`get()`]()
    - to retrieve the current text from an Entry widget
- []()
- []()
- []()
- []()

- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- [`insert()`](#insert)
- [`invoke()`]()
    - programmatically trigger a button's command
- []()
- []()
- []()
- []()
- []()
__________________________________________________________________________________________________________


## Universal Methods
- a set of methods that are available and can be applied all or most Tkinter widgets, including the main Tk() window itself
- these methods provide common functionalities that are useful across various GUI elements
- provide a consistent way to interact with and manage various aspects of Tkinter widgets, regardless of their specific type

#### Universal Methods
- [`after(delay_ms, callback=None, *args)`](#after)
    - schedules a callback function to be executed after a specified delay_ms milliseconds
- [after_cancel(after_id)]() 
    - used to cancel a scheduled callback that was set up using `after()`
- [after_idle(func, *args)]() 
    - schedules a func to be called when Tkinter is idle, meaning there are no pending events to process
- [bell()]()
    - emits an audible sound, typically a system beep
- [`bind()`]()
    - to associate events (like clicks or key presses) with specific functions
- [`config()`]()
    - to change options like text, color, or font
- [`disable()` or `enable()`]()
    - to change the widget's interactive state
- [focus_get()]() 
    - returns the widget that currently has the keyboard focus
- [focus_set()]()
    - sets the keyboard focus to the specified widget
- [`grid()`]()
- [`pack()`]()
- [`place()]()
- [winfo_exists()]()
    - returns a boolean indicating whether the widget's underlying Tcl interpreter object still exists
- [winfo_id()]()
    - returns the unique Tcl identifier for the widget
- [winfo_parent()]()
    - returns the parent widget of the current widget
- [winfo_children()]()
    - returns a list of all child widgets of the current widget



