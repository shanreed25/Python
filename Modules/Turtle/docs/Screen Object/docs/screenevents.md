# Turtle Module: Screen Events
- screen events are actions or occurrences that happen within the Turtle graphics window
- they allow you to create interactive programs
- Common Screen Events
    - Keyboard events
    - Mouse events
    - Window events
    - Timer events


# Handling Events
**To respond to these events, you need to:**
- Define a function (event handler): will be called when the event occurs
- Bind the event handler to the event: using specific Turtle methods to connect the event to the function you want to run
- Start listening for events: call the `screen.listen()` method to instruct the Turtle screen to watch for events
- always call `screen.listen()` before your event bindings and` turtle.done()` or `mainloop()` at the end of your script to keep the window open and responsive to events. 


# Keyboard events
- occur when a user presses or releases keys on the keyboard
- `onkey(function, key):` Binds a function to a key-release event
- `onkeypress(function, key):` Binds a function to a key-press event. You can also bind it to any key press by omitting the key argument

# Mouse Events
- actions like clicking a mouse button, releasing a mouse button, or dragging the mouse
- **onclick(function, btn=1, add=False) or onscreenclick(function, btn=1, add=False):** Binds a function to a mouse-click event on the screen or on the turtle itself.
- **onrelease(function, btn=1, add=False):** Binds a function to a mouse-button-release event.
- **ondrag(function, btn=1, add=False):** Binds a function to a mouse-drag event.

# Window Events
- can include events like closing the Turtle graphics window

# Timer Events
- are scheduled events that occur after a specified time interval
- **ontimer(function, t=0):** Installs a timer that calls the function after t milliseconds

# `onscreenclick()
```
# TODO: Get x and y values when you click on the screen
def get_mouse_click_cor(x,y):
    print(x,y)

# when the screen is clicked, it returns the x and y coordinates
turtle.onscreenclick(get_mouse_click_cor)
```