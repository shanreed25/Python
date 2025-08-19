# Special Attributes
- also known as "dunder" attributes due to their double leading and trailing underscores `__name__`
- built-in attributes that provide access to internal object and class information
- they are part of Python's data model and are used for various purposes, including introspection, customization of object behavior, and providing metadata.

# Decorators
- allow you to modify or extend the behavior of functions or methods without directly altering their original source code
- they "wrap" a function, adding functionality before, after, or even in place of the original function's execution
- typically applied using the `@decorator_name` syntax placed immediately above the function definition you want to decorate
- is syntactic sugar for function_name = decorator_name(function_name)
- imagine that you have a bunch of functions in a class or module and you want to add some functionality to each of these functions, a decorator function can help you do this