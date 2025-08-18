# Dictionary Comprehension
- a concise and efficient way to create a new dictionary based on an existing iterable (like a list, tuple, range or another dictionary)
- provides a more compact and readable syntax compared to using traditional for loops and dict.update() or dict.setdefault() methods
- **Conciseness:** Reduces the amount of code needed to create dictionaries.
- **Readability:** Can make the code more understandable, especially for simple transformations.
- **Efficiency:** Often performs better than equivalent for loop constructions for creating new dictionaries.
___________________________________________________________________________________________________

# Keyword Method
- when reading a list comprehension it can be hard to understand the structure and flow of the comprehension
- the keyword method helps with understanding  the structure and flow of the comprehension
- the keyword method involves
    1. typing out the list comprehension keywords
    2. then replace each of the words with the actual item in your code

# Dictionary Comprehension Types
**While there is only one type of dictionary comprehension, it can be used in various forms or applications depending on the desired outcome**

- **Dictionary Comprehension Basic Syntax:** `new_dict = {key_expression: value_expression for item in iterable}`
    - **key_expression:** an expression that determines the key for each item in the new dictionary.
    - **value_expression:** an expression that determines the value for each item in the new dictionary.
    - **item:** a variable that represents each element from the iterable during the iteration.
    - **iterable:** the source collection (e.g., list, tuple, set, another dictionary's items(), keys(), or values()) from which the items are processed

- **Conditional filtering:**`new_dict = {key_expression: value_expression for item in iterable if condition}`
    - an if statement can be added to include only specific items based on a condition

**Conditional value assignment:** `new_dict = {key: (value_if_true if condition else value_if_false) for item in iterable}`
    - an if/else expression can be used within the value_expression to assign different values based on a condition

# See Dictionary Examples [here](https://github.com/shanreed25/Python-Cheatsheet/tree/main/DataStructures/Dictionaries)