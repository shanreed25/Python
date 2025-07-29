
# print()
- print is used to display a value to the console for the programmer to see

# Docstring
    You can use docstrings to write multiline comments
- Just enclose your text inside a pair of three double quotes.

# Colons (:)
- The colon acts as a structural element in Python, guiding the interpreter on how to interpret the code that follows,
- Especially regarding the organization and execution of code blocks
- In Python, a colon (:) is used in various ways, but primarily, it serves to indicate the start of an indented block of code or to denote special syntax within expressions. 







- # Rename something and it change for all instances of that name: right click refactor rename

# PascalCase for class names

# snake_case for almost everything else

```
""" 
My 
Multiline 
Comment 
"""

```
### Documenting Functions
- you can use docstrings to display text when you hover over a function call
- helps you remember what a function does
- use docstring just below the function definition and that text will be displayed when you hover over the function call


```
def my_function(num):
    """Multiplies a number by itself."""
    return num * num
```


## Variables
- You can create a variable that represents the absence of a value or a "null" state, using the "None" Keyword
  - `my_var = None`
  - the closest equivalent to an "undefined" variable in Python


- when working with code that comes after : and you want to  hold on to a variable

# Common uses for `pass`
- Placeholder in empty code blocks
  - Python requires code blocks (e.g., after if, elif, else, for, while, def, class) to contain at least one statement
  - if no action is needed for a particular block, `pass` can be used to avoid a SyntaxError
- Prototyping and scaffolding
  - When designing a program, pass allows for the creation of function or class stubs
  - outlining the structure without immediately implementing the logic
  - This facilitates a top-down development approach
- Temporarily disabling code
  - pass can be used to temporarily comment out or disable a block of code without removing it entirely
  - this prevents its execution without causing syntax errors








  Here are the main contexts where the code after a colon is used:
1. Defining code blocks
Function definitions: The colon marks the start of a function's body.
python
def greet(name):
    print(f"Hello, {name}!") # This is the code block after the colon
```
Class definitions: Similarly, the colon signals the beginning of a class's attributes and methods.
python
class Dog:
    def bark(self):
        print("Woof!") # This is the code block after the colon
```
Conditional statements (if, elif, else): The code after the colon is executed if the corresponding condition is met.
python
x = 10
if x > 5:
    print("x is greater than 5") # This is the code block after the colon
```
Loop structures (for, while): The colon indicates the block of code that will be executed repeatedly.
python
for item in ["apple", "banana", "cherry"]:
    print(item) # This is the code block after the colon
```

 
2. Slicing sequences
When used within square brackets ([]) with sequences like lists, tuples, and strings, the colon is used for slicing, defining a sub-sequence based on start, stop, and step values.
python
my_list = [1, 2, 3, 4, 5]
slice_of_list = my_list[1:4]  # Extracts elements from index 1 (inclusive) to 4 (exclusive)

3. Dictionary key-value pairs
In dictionary literals, the colon separates a key from its corresponding value.
python
my_dictionary = {"name": "Alice", "age": 30} # "name" and "age" are keys, separated by colon from values "Alice" and 30

4. Type hints
Python uses colons to provide type hints for variables, function parameters, and return values, enhancing code readability and allowing static analysis tools to check for potential type mismatches.
python
def add(a: int, b: int) -> int: # 'a' is hinted to be an integer, 'b' is hinted to be an integer, and the function is hinted to return an integer
    return a + b
