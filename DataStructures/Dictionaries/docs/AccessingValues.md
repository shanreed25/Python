# Accessing Dictionary Values
- here are several ways to access values in a Python dictionary


## Square Brackets []
- the most common and direct way to access a value by its key
- if the key does not exist, this method will raise a KeyError
- use the the get() Method to avoid the KeyError, if the key does not exist


## get() Method
- provides a safer way to access values
- allows you to specify a default value to return if the key is not found, instead of raising an error
- if you do not provide a default value it will return None, instead of raising an error
- `get("number")`
    - Returns None if the number key is not found
- `.get("number", "Unknown")`
    - Returns "Unknown" if "number" key is not found


## values() method
- returns a view object that displays a list of all the values in the dictionary
- you can iterate over this view to access all values

## items() method
- returns a view object that displays a list of a dictionary's key-value tuple pairs
- can unpack these tuples in a loop to access both keys and values