# Tuple
an ordered, immutable sequence of elements
- once a tuple is created, its elements cannot be changed, added, or removed
- defined by enclosing comma-separated values within parentheses ()
- are heterogeneous, which mean it can contain elements of different data types
- `(5, 20, 13, 35, 98)`
- single-element tuple requires a trailing comma
  - `('hi',)`
- support various operations
  - including concatenation using `+`, repetition using `*`, and membership testing using `in` and `not in`

# Use Cases:
- Returning multiple values from a function
  - functions can easily return multiple values as a tuple
- Data integrity
  - when you need to ensure that a collection of data remains unchanged
  - tuples provide a "write-protect" mechanism
- Dictionary keys
  - Because tuples are immutable and hashable (if their elements are also hashable), 
    - they can be used as keys in dictionaries, unlike mutable lists
- Data unpacking
  - Tuple packing and unpacking allow for convenient assignment of multiple values to multiple variables