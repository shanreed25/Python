# Python commonly use built in functions


# len(data_type): used to determine the length or number of items in an object
- can be applied to various data types that represent sequences or collections
- count the number of items in
  - a string
  - a list
  - a dictionary(key-value pairs)
  - a tuple
  - a set
## Underlying mechanism:
For built-in types, len() directly accesses the length information stored within the object's internal 
structure for efficiency. For custom classes, len() works by calling the object's __len__ special 
method. If a custom class does not define this method, calling len() on an instance of that 
class will result in a TypeError.