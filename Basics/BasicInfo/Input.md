# Python Input
- input operations are fundamental for interacting with users and external systems
- the primary function for basic input is `input()`, and it is used to obtain data from the user through the keyboard
- `input()` pauses program execution and waits for the user to type something and press enter
    - the value entered by the user is returned as a string
- an optional prompt string can be passed to `input()` to display a message to the user before they enter their data
    - `name = input("Enter your name: ")`


### Type Conversion for Input
- since `input()` always returns a string, explicit type conversion is often necessary when numerical or other data types are expected
- use `int()` to convert a string to an integer
- use `float()` to convert a string to a floating-point number
- `age = int(input("Enter your age: "))`