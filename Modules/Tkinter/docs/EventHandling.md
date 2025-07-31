# Event Handling
- handling events in Tkinter primarily involves two mechanisms: 
    - `command`: option for specific widget actions
    - `bind()`: method for more general event binding


## `command` option
- many widgets, such as Button, Checkbutton, Radiobutton, and Scale, have a command option
- allows you to directly associate a function (a "callback") that will be executed when a specific, predefined event occurs for that widget such as a button click
    ```
    def action():
    print("Button was clicked!")

    my_button = Button(command=action)

    ```

## `bind()` method
- provides a more versatile way to handle a wider range of events
    - including keyboard presses, mouse clicks, mouse movement, window resizing, and more
- allows you to bind a specific event sequence to a handler function for a widget or even the entire application