# Lambda Functions
- are small, single-expression functions that do not require a formal def statement and a name
- use keyword  `lambda` to create anonymous/lambda functions
- Anonymous: They are not defined with a name using the def keyword.
- **Single Expression:** can only contain a single expression, which is implicitly returned
    - You cannot have multiple statements or complex logic within a lambda
- **Concise Syntax:** offer a more compact way to define simple functions
- **Usage:** lambda functions are often used in situations where a small, temporary function is needed, especially as arguments to higher-order functions like map(), filter(), sorted(), and reduce().
- `lambda arguments: expression`

    ```
    # A lambda function to square a number
    square = lambda x: x * x
    print(square(5)) # Output: 25

    # Using lambda with map()
    numbers = [1, 2, 3, 4]
    squared_numbers = list(map(lambda x: x * x, numbers))
    print(squared_numbers) # Output: [1, 4, 9, 16]
    ```



#### Explanation of `command=lambda: [function1(), function2()]` in Tkinter
In Tkinter, the command attribute of a button expects a single callable (a function or method) that will be executed when the button is pressed. When you want a button to trigger multiple functions, you need to provide a single callable that, in turn, calls those multiple functions. This is where lambda: [function1(), function2()] comes into play. 
Breakdown
lambda: This keyword creates an anonymous (unnamed) function in Python. It's a concise way to define small functions, especially when you only need them for a specific purpose and don't want to formally declare them with def. In this case, the lambda function takes no arguments, indicated by the empty parentheses after lambda.
[function1(), function2()]: This is a list containing the results of calling function1() and function2(). When the button is clicked, the lambda function is executed, which in turn evaluates this list. Since each element in the list is a function call (e.g., function1()), both function1 and function2 are executed in sequence when the button is clicked. 
How it works
When the button is clicked, the lambda function associated with the command attribute is invoked. The lambda then executes the expressions within its body, which in this case are the calls to function1() and function2(). This allows you to effectively bind multiple functions to a single Tkinter button click. 

### Alternatives
Creating a named function that calls the desired functions can achieve the same result as lambda: [function1(), function2()]. This named function can then be assigned to the button's command. 
python
import tkinter as tk
```
def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

def combined_actions():
    say_hello()
    say_goodbye()

root = tk.Tk()

button = tk.Button(root, text="Click Me", command=combined_actions)
button.pack()

root.mainloop()
```
This approach can improve readability in complex scenarios or when you need to pass arguments to the functions being called. 