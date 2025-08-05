# Dictionaries
Dictionaries allow us to group together and tag related pieces of information, and functions similarly to a dictionary in real life. 
It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.
- Every dictionary has two parts
  - Key: equivalent of a word, in a real life dictionary
  - Value: equivalent of the definition of a word, in a real life dictionary
`emp_phone_numbers = {"Lisa": 123-456-7890}`

##### Key
- items are identified/accessed by the key, and counting starts at 1
- if you try to retrieve, but you spell the key wrong you will get a
  - `KeyError`: which means the key does not exist and cannot be found
- keys must be the correct data type: `emp_phone_numbers = {Lisa: 123-456-7890}`
  - will cause a: `NameError: name 'Lisa' is not defined.`
  - Python thinks that Lisa is variable you declared somewhere


##### Remove and return item by index: `dict.pop(key)`
- used with lists and dictionaries to remove and return an element
- removes the key-value pair associated with the specified key from the dictionary
- returns the value associated with the removed key
- If the key is not found and no default_value is provided, a `KeyError` will be raised.
  - Syntax with default value: `dict.pop(key, default_value)`

##### Accessing Dictionary Values
- there are several ways to access values in a Python dictionary
- **Square Brackets []**
- **get() Method**
- **values() method**
- **items() method**

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





___________________________________________________________________________________________
# See Dictionary Examples [here](https://github.com/shanreed25/Python-Cheatsheet/blob/main/DataStructures/dictionaries.py)
  - Accessing Values Examples 
  - Looping Through A Dictionary Examples
  - Using methods like max(), pop(), items(), etc.....
- Dictionary Comprehensions





_____________________________________

