# Functions
- self-contained block of organized, reusable code designed to perform a specific task
- break down complex problems into smaller, manageable units, making code easier to understand, debug, and maintain
- defined independently, not associated with any particular object or class
    - a [method](../Methods/methods.md) is a function that belongs to a class and is defined within that class
- are defined using the `def` keyword, followed by the function name, parentheses (which may contain parameters), and a colon. The code block within the function is indented
    - can accept data inputs through **parameters** defined in their definition
    - when calling the function, values passed to these parameters are known as **arguments**
    - can optionally return output values using the return statement, if no return statement is present, the function implicitly returns None
- can be called directly by its name from anywhere in the program where it is in scope
    - code only executes when it is explicitly called by its name followed by parentheses
- typically operate on data passed to them as arguments and can return values
**Functions are general-purpose procedures. They are like tools you can use independently**

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