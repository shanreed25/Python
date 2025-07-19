# try/except block
- the try-except statement is used for handling exceptions that might occur
- it allows you to gracefully manage errors and prevent your program from crashing
- For example if you imagine there could be a chance of user error
  - You can prevent it crashing your code by anticipating it
- You trap the dangerous code inside a try block and use an except block to catch any potential errors
- Then you define what should happen when that error occurs instead of simply just crashing and stopping the code.

# How try-except works
- `try` block: contains the code that might potentially raise an exception
  - Python attempts to execute the code within this block
- `except` block(s): if an exception occurs within the try block
  - Python immediately stops executing the try block and looks for a matching except block to handle the specific exception that occurred.
  - You can specify different except blocks to handle different types of exceptions
  - or a general except block to catch any unhandled exception
  - it's generally recommended to catch specific exceptions for better error management
- `else` block (optional): This block is executed only if no exception occurs within the try block.
- `finally` block (optional): This block is always executed
  - regardless of whether an exception occurred or not, or if it was handled
  - often used for cleanup operations, like closing files or releasing resources.
```

# if user enters a number as a word(one, three, ten)
# it will produce a ValueError: invalid literal for int() with base 10: 'ten'
# you can use a try/catch block to catch this error
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")


try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid input: Please enter numerical number such as 20")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You can not drive at age {age}.")
```