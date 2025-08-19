# Special Attributes
- also known as "dunder" attributes due to their double leading and trailing underscores `__name__`
- built-in attributes that provide access to internal object and class information
- they are part of Python's data model and are used for various purposes, including introspection, customization of object behavior, and providing metadata
- provide access to the internal workings and metadata of objects, classes, and modules
- special attributes are a fundamental part of Python's design, enabling powerful and flexible object-oriented programming
- Special Attributes [docs](https://docs.python.org/3/library/stdtypes.html#special-attributes)


### `__name__`
- the `__name__` variable in Python holds the name of the current module or package
- you can tap into `__name__` to find out what the name of the current class, function, method, descriptor or generator
- when you run a Python script directly, `__name__` is set to `__main__`
- when a Python file is imported as a module into another script, `__name__` is set to the actual name of the module
- `print(__name__)`
    - if it prints `__main__` it means a module’s `__name__ `is set equal to `__main__` 
    - which means it is being read from standard input, a script, or from an interactive prompt but not from an imported module 
        - https://docs.python.org/3.9/library/__main__.html
- `app = Flask(__name__): print(__name__)`
    -  prints `__main__` when the application is being run directly as a script and not imported as a module within a larger project
- `print(random.__name__)`
    - prints `random` because it is read from a module
    - when a Python file is imported as a module into another script, __name__ is set to the actual name of the module