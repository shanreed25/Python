# Function Compoenents

### Function Definition
- **def** : function **def**inition
- **funcName():**: function name followwed by a set of () and a :(colon) `myFunction():`
- **Function definition**: `def myFunction():`

### Function Body
- **function body:** the code that goes inside the function
    ```
    def myFunction():
        function body goes here
    ```
- **function call:** `myFunction()`

    ##### Basic Function
    ```
    def sayHello():
        print("Hello")
        
    sayHello() # will print "Hello"
    ```

### Return Statement
- the return statement is used to give back a value from a function which can be used later
  - print is used to display a value to the console for the programmer to see
- functions terminate at the return keyword, so any code after the return statement will not be executed
  - you can have multiple return statement(Conditional return)
- when the function is called it will run then output the result
- the result replaces the function call
    ```
    def add():
        return 5 + 2
    print(add())  # will return 7
    ```
    - 7 will replace the function call

#### Conditional Return
- multiple return statements based on certain conditional checks(control flow)

#### Empty return
- return without anything after, this just tells the function to exit

### Function Parameters
- you can customized functions by providing input values called parameters
- these input values are known as arguments when the function is called
    - you provide the actual values (arguments) inside the parentheses when calling the function
    - these arguments are then assigned to the corresponding parameters in the order they are defined
- parameters are declared within the parentheses when defining the function
- each parameter acts as a local variable within the function's scope, holding the value of the corresponding argument passed during the function call
- [More](./CustomizedFunctions.md)

### Storing Functions as a Variable Value
- You can store a reference to a function as a value to a variable
- add the function name without parentheses, as the value to the variable

    ```
    def add(n1, n2):
        return n1 + n2

    my_add_function = add
    print(my_add_function(3, 5)) # Will return 8
    ```
- this also works with dictionaries, you can store a function as the value to a key

    ```
    operation_functions = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    # Syntax to call the multiply function
    print(operation_functions["*"](5, 5))
    # Example from Calculator Project
    ```

