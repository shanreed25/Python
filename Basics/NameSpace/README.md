# Namespace
- Namespaces are crucial for organizing code and preventing naming conflicts
- In Python, a namespace is a mapping from names to objects
- functions like a dictionary
  - keys are the names (identifiers) you use in your code
  - values are the corresponding objects (variables, functions, classes, modules, etc.) that those names refer to in memory
- Understanding namespaces is fundamental to comprehending how Python manages names and objects, and how code is organized and executed


# Key characteristics of Python namespaces
- Mapping from names to objects
    - they essentially keep track of what each name in your code refers to.
- Preventing naming conflicts
  - Different namespaces can contain the same name without causing issues, as long as they are distinct
  - For example, `math.sqrt` and `cmath.sqrt` refer to different sqrt functions in their respective module namespaces.
- Scope and lifespan
  - Namespaces are created and destroyed as different parts of your program execute
  - The scope of a name determines which namespaces are searched to resolve that name

# Built-in Namespace
- Contains all the pre-defined names available in Python, such as print(), len(), True, False, etc
- This is the outermost namespace

## Classes and Objects:
- Classes define their own namespaces for attributes and methods 
- instances of those classes also have their own namespaces for instance-specific attributes.

# How Namespaces are Used