# Python Typing
- Python is classified as both a dynamically typed and a strongly typed language due to distinct characteristics in its type system
- typing refer to how a programming language handles data types, specifically when type checking is performed
- In some programming laguages(C, Java, Swift etc...), once you create a variables and give it a certain data type of data, that variable can only hold on to that data type
- python allows you to change the data type of a variable just by assigning it to a different type of value

# Strongly Typed
- strong typing ensures that operations are only performed on compatible data types, leading to more predictable and robust code
- **Type Coercion Prevention:** prevents implicit type conversions between incompatible types       
    - operations between different types require explicit type casting or conversion
    - prevents unexpected behavior and ensures type safety
    - `result = "10" + 20`
        - this will raise a TypeError, as string and integer cannot be implicitly added
        - you would need to explicitly convert one of the types

**The type of value doesn't change in unexpected ways, every change of a type requires explicit conversion**
______________________________________________


# Dynamically Typed
- **Runtime Type Determination:** the type of a variable(type checking) is determined at [run time](./ComplieVsRunTime.md)(as the code is running), not at compile time
    - this means you do not explicitly declare the data type of a variable when you create it
    - the Python interpreter infers the type based on the value assigned to the variable
- the opposite of dynamic typing is static typing
    - with static typing variable types are declared at [compile time](./ComplieVsRunTime.md)(before the code is executed) and cannot be changed during runtime
**Runtime objects(the actual values), have a type
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ```
        x = 10       # x is an integer
        x = "hello"  # Now x is a string
    ```