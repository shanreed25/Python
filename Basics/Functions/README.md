# Functions
- self-contained block of organized, reusable code designed to perform a specific task
- defined independently, not associated with any particular object or class
    - a [method](../Methods/methods.md) is a function that belongs to a class and is defined within that class
- can be called directly by its name from anywhere in the program where it is in scope
- typically operate on data passed to them as arguments and can return values
**Functions are general-purpose procedures. They are like tools you can use independently**

## Functions
- named blocks of reusable code that perform specific tasks
- You define functions using the def keyword, followed by the function name, parentheses containing optional parameters, and a colon.
- Functions can take input values (arguments) and optionally return output values using the return statement.
- Defining and using functions helps to organize your code, make it more modular, and promote reusability. 

_________________________________________________
#### Definition 
- Functions are defined using the def keyword, followed by the function name, parentheses (which may contain parameters), and a colon. The code block within the function is indented.
#### Execution
- A function's code only executes when it is explicitly called by its name followed by parentheses.

#### Parameters and Arguments
- Functions can accept data inputs through parameters defined in their definition. When calling the function, values passed to these parameters are known as arguments.
#### Return Values
- Functions can return a value or object using the return statement. If no return statement is present, the function implicitly returns None.
#### Reusability
- Functions allow the same code logic to be executed multiple times with different inputs, reducing code duplication and making programs more efficient.
#### Modularity
- Functions break down complex problems into smaller, manageable units, making code easier to understand, debug, and maintain.
________________________________________________________________________
**Python functions can be categorized into several types based on their origin and behavior**
- [Built-In Functions](./docs/builtinfunctions.md)
    - These are functions pre-defined in Python and readily available for use without any explicit definition. Examples include print(), len(), type(), sum(), min(), and max()
- [User-defined Functions]()
    - These functions are created by the programmer to perform specific tasks. They are defined using the def keyword, followed by the function name, parameters (if any), and the function body
- [Higher-Order Functions](./docs/higher-order-functions.md)
    - These functions can take other functions as arguments or return functions as their results. 
- [Lambda Functions (Anonymous Functions)]()
    - These are small, single-expression functions that do not require a formal def statement. They are defined using the lambda keyword and are often used for short, inline operations
- [Recursive Functions:]()
    - These functions call themselves to solve a problem by breaking it down into smaller, similar sub-problems. They require a base case to prevent infinite recursion
- [Generator Functions:]()
    - These functions use the yield keyword to produce a sequence of values one at a time, rather than returning a single value. They are memory-efficient, especially for large sequences
- []()
- []()
- []()
- []()
- []()