# Widget Methods



# `after()`
- a universal widget method used to schedule a function to be called after a specified delay
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

## Key Features and Usage
- **Scheduling a one-time event:** The most common use case is to execute a function once after a certain time. For instance, to close a window after 5 seconds
- **Creating periodic tasks:** By calling `after()` recursively within the callback function, you can create tasks that run repeatedly at regular intervals. This is useful for animations, updating sensor readings, or other continuous processes
- **Non-blocking execution:** Unlike time.sleep(), which blocks the entire program, `after()` schedules the callback to be run by the Tkinter event loop. This ensures that the GUI remains responsive and interactive while the delay occurs
- **Cancellation:** The `after()` method returns an integer "after identifier." This identifier can be passed to the `after_cancel()` method to cancel a scheduled callback before it executes
- **after_idle():** A related method, `after_idle()`, schedules a function to be called when the Tkinter event loop is idle, meaning there are no pending events to process. This is useful for tasks that should run when the system is not busy
__________________________________________________________________________________________________________