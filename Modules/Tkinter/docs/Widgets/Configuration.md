# Widget Configuration
- widgets can be configured in several ways to modify their appearance and behavior
    - During Widget Creation
    - Using the configure() Method
    - Using Dictionary-Style Access
    - Using StringVar or other Tkinter Variables
- specific configuration options vary by widget type




## During Widget Creation
- configuration options can be passed as keyword arguments when creating a widget instance
- the most common and straightforward method for initial setup
- `canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)`

## Using the configure() Method
- allows you to change one or more configuration options of a widget after it has been created
- useful for dynamic updates based on user interaction or program logic
- alias for `configure()` is `config()`

## Using Dictionary-Style Access
- you can access and modify widget options using a dictionary-like syntax
- is essentially a shorthand for `configure()`
- `button["text"] = "Start"`



## Using StringVar or other Tkinter Variables
- options like text in Label or Entry widgets, can be linked to a Tkinter variable (StringVar, IntVar, DoubleVar, BooleanVar etc...)
- changes to the variable will automatically update the widget
- Steps:
    1. Create a StringVar
    2. Associate StringVar with the widget
    3. Set the initial text using the `set()`
        - you can also update the value using `set()`
        - you can get the text value using the `get()` method

    ```
        greeting = Label()
        greeting.pack()

        # Create a StringVar:
        greeting_str_var = StringVar()

        # Associate StringVar with the widget: set its textvariable option to the StringVar
        greeting.config(textvariable=greeting_str_var)


        # Set the initial text: use the set() method of the StringVar
        greeting_str_var.set("Hello")

        def greet(text):
        # Update the text: : use the set() method of the StringVar
        greeting_str_var.set(text)

        # Window will wait 1 second then call the greet("Goodbye")
        window.after(1000, greet, "Goodbye" )
    ```