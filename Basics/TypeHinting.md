# Type Hinting 
**The process of adding type hints encourages developers to think more explicitly about data flow and the types involved in their code. This can lead to more robust and well-structured designs, especially when dealing with complex systems.**
- just a way to indicate the expected types of variables, function parameters, and return values
- type hints can be used for better code readability and static analysis tools
- it does not enforce the type at runtime so, Python's dynamic typing still applies
- a form of inline documentation, making it easier for developers to understand the expected data types for a function's inputs and outputs
- enhances code comprehension and maintainability, especially in larger or collaborative projects
- Tools like mypy or pyright can leverage type hints to perform static type checking on your code before it runs
- helps with the early detection of potential type-related errors, reducing the likelihood of runtime bugs and improving code quality

**IDE's and linters can utilize type hints to provide more intelligent features, such as**
- Code Completion: Suggesting relevant methods and attributes based on the inferred type of an object.
- Error Checking: Highlighting potential type mismatches or incorrect usage.
- Refactoring: Assisting with safe code modifications.
- Better Code Design and Architecture:


- `age; int`: indicates that age is expected to hold an integer value
- `def check_id(age: str)`: indicates that the check_id function expects a string as an input
- `def check_id(age: str) -> bool`: specify the output of the data type of a function