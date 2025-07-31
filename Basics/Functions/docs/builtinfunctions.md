# Python commonly use built in functions


# len(data_type): used to determine the length or number of items in an object
- can be applied to various data types that represent sequences or collections
- count the number of items in
  - a string
  - a list
  - a dictionary(key-value pairs)
  - a tuple
  - a set

# Functionality
- returns an integer representing the count of items within the object.
- can be applied to various data types, including:
  - **Sequences:** Strings, lists, tuples, bytes, range objects. For these, it returns the number of elements or characters.
  - **Collections:** Dictionaries, sets, frozen sets. For these, it returns the number of key-value pairs (for dictionaries) or unique elements (for sets).
- **Parameter: object:** (sequence or collection) whose length is to be determined.
- **Return Value:** integer representing the length of the object
- **Examples:**
  - string: `len("Hello")`: Output: 5
  - list: `len([1, 2, 3, 4, 5, 6, 7])`: Output: 7
  - dictionary: `len({"name": "Shannon", "age": 37, "phone_number": 1234987645})`: Output: 3
  - set: `len({1, 2, 3, 4, 5, 2, 4})`: Output: 5 (duplicates are removed in sets)

## Underlying mechanism:
For built-in types, len() directly accesses the length information stored within the object's internal 
structure for efficiency. For custom classes, len() works by calling the object's __len__ special 
method. If a custom class does not define this method, calling len() on an instance of that 
class will result in a TypeError.

# List and set functions
In Python, list() and set() are built-in functions used to create or convert to list and set data structures, respectively.
list()
The list() function creates a new list. It can take an iterable (like a tuple, string, set, or another list) as an argument, converting its elements into a new list. If no argument is provided, it creates an empty list.

# set()
set()
The set() function creates a new set. It takes an iterable as an optional argument, converting its elements into a new set. A key characteristic of sets is that they only store unique, hashable elements and do not maintain order. If the iterable contains duplicates, set() will automatically remove them. If no argument is provided, it creates an empty set.
- # TODO:Remove duplicates from the List: does not guarantee the order of elements in the resulting list
colors_list = list(set(squirrel_color_list))

________________________________________________________________________________

