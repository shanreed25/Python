# Exceptions
- exceptions are events that disrupt the normal flow of a program execution
- it signals that an error or exceptional condition has occurred
- exceptions are runtime errors, meaning they arise during the program's execution
  - opposed to syntax errors which are detected by the Python interpreter during parsing

# Exception Handling
- Python provides a mechanism to handle these exceptions gracefully using `try`, `except`, `else`, and `finally` blocks
- The try block contains the code that might raise an exception
- The except block specifies how to handle a particular type of exception if it occurs within the try block
- The else block (optional) executes if no exception is raised in the try block
- The finally block (optional) always executes, regardless of whether an exception occurred or was handled

# Raising Exceptions
- You can explicitly raise exceptions using the raise statement to signal an error or unusual condition in your code
- can be done for both built-in exceptions and custom exceptions

# Built-in Exceptions
- Python includes a wide range of built-in exceptions for common error scenarios, such as:
  - ZeroDivisionError: Attempting to divide by zero.
  - TypeError: An operation or function is applied to an object of an inappropriate type.
  - FileNotFoundError: Attempting to open a file that does not exist. 
  - IndexError: An index used to access a sequence (like a list) is out of bounds.
  - KeyError: A key used to access a dictionary does not exist. 

# Custom Exceptions
- You can define your own custom exception classes by inheriting from Exception or one of its subclasses
- This allows for more specific error handling tailored to your application's needs

# Benefits of Exception Handling:
- Robustness: Prevents programs from crashing due to unexpected errors.
- User-friendliness: Allows for providing informative error messages to users instead of cryptic tracebacks.
- Code Clarity: Separates error-handling logic from the main program flow, making code more readable.