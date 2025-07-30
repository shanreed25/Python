# Widget Methods
- [`after()`](#after)
- [`after_cancel()`](#after_cancel)
- []()
- []()
- [`focus()`](#focus-or-focus_set)
- []()
- []()
- [`insert()`](#insert)
- []()
- []()


# `after()`
- a universal widget method used to schedule a function to be called after a specified delay
- primary use of after() is to introduce a delay before executing a specific function
- crucial for creating dynamic and responsive graphical user interfaces (GUIs) in Tkinter
- allows for non-blocking execution of tasks within the Tkinter event loop, preventing the GUI from freezing during operations that require a delay
    - allows for delayed execution of code without blocking the main event loop, which would otherwise freeze the GUI
- **Syntax:** `widget.after(delay_ms, callback=None, *args)`
- **Parameters**
    - **delay_ms:** the amount of time it should wait in milliseconds
    - **callback:** function you give it, that will be called after the time has expired
        - If None, the `after()` method simply pauses the execution of the current thread for the specified delay_ms, similar to time.sleep(), but within the Tkinter event loop.
    - ***args:** optional arguments to be passed to the callback function.
- **Example:**
    ```
        def say_hello(name, city):
        print(f"Hello, {name} from {city}")


        window.after(5000, say_hello, "Shannon", "Las Vegas")   

    ```
        - `say_hello("Shannon", "Las Vegas")` will be called after 5 seconds

#### Key Features and Usage
- **Scheduling a one-time event:** The most common use case is to execute a function once after a certain time. For instance, to close a window after 5 seconds
- **Creating periodic tasks:** By calling `after()` recursively within the callback function, you can create tasks that run repeatedly at regular intervals. This is useful for animations, updating sensor readings, or other continuous processes
- **Non-blocking execution:** Unlike time.sleep(), which blocks the entire program, `after()` schedules the callback to be run by the Tkinter event loop. This ensures that the GUI remains responsive and interactive while the delay occurs
- **Cancellation:** The `after()` method returns an integer "after identifier." This identifier can be passed to the `after_cancel()` method to cancel a scheduled callback before it executes
- **after_idle():** A related method, `after_idle()`, schedules a function to be called when the Tkinter event loop is idle, meaning there are no pending events to process. This is useful for tasks that should run when the system is not busy
__________________________________________________________________________________________________________

# `after_cancel()`
- used to cancel a scheduled callback function that was previously set up using the `after()` method
- `after()` method returns an integer "after identifier" (often referred to as an "after ID")
    - `after_id = window.after(3000, count)`
- to prevent the scheduled function from executing, you call `widget.after_cancel(after_id)`, passing the after_id that was returned by the original after() call

__________________________________________________________________________________________________________

# `delete()`
- is used to remove characters or content from certain widgets, primarily Entry and Text widgets
- removes content within a widget

__________________________________________________________________________________________________________

# `focus()` or `focus_set()`
- When a Tkinter application has multiple input fields it allows you to programmatically determine which one should be active and ready to receive typed characters
- use it to set the initial focus to a particular widget when a window or application starts, making it immediately ready for user interaction
- **Entry Widget:** `entry_widget.delete(first_index, last_index=None)`
    - **first_index:** The starting index of the character(s) to be deleted (0-indexed)
    - **last_index (optional):** The ending index of the character(s) to be deleted. If omitted, only the character at first_index is deleted. To clear all content, use END as the last_index
- **Text Widget:**
    - **first_index:** The starting index in the format "line.character" (e.g., "1.0" for the beginning of the first line).
    - **last_index (optional):** The ending index. If omitted, only the character at first_index is deleted. To clear all content, use END

__________________________________________________________________________________________________________

# `insert()`
- used to add text or items into various widgets, primarily Entry, Text, and Listbox widgets
- specific usage and arguments depend on the widget type
- `widget.insert(index, string)`
    - **index:** The position at which to insert the text. This can be an integer (0 for the beginning, 1 for the second character, etc.) or tk.END to append to the end.
    - **string:** The text to be inserted
- **Entry Widget** index can be an integer (0 for the beginning, 1 for the second character, etc...) or `END` to append to the end
- **Text Widget** index is typically in the format "line.character": "1.0" for the beginning of the first line, "5.5" for the 6th character of the 5th line
    - constants like `INSERT` (at the insertion cursor) and `END` (at the end of the entire text) can also be used
- **ListBox Widget:** `listbox.insert(index, *items)` can insert one or more items
    - index can be an integer (0 for the beginning, 1 for the second item, etc.) or tk.END to append to the end.
__________________________________________________________________________________________________________