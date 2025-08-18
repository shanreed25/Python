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
- keys must be unique
  - if you try to add an item to a dictionary using a key that already exists, the new value you provide will overwrite the existing value associated with that key

##### Remove and return item by index: `dict.pop(key)`
- used with lists and dictionaries to remove and return an element
- removes the key-value pair associated with the specified key from the dictionary

##### Accessing Dictionary Values
- there are several ways to access values in a Python dictionary
- **Square Brackets []**: most common way to access values
- **get() Method**: safer way to access values
- **values() method**: returns a view object that displays a list of all the values in the dictionary, you can iterate over this view to access all values
- **items() method**: returns a view object that displays a list of a dictionary's key-value tuple pairs, you can unpack these tuples in a loop to access both keys and values

___________________________________________________________________________________________
# See Dictionary Examples [here](https://github.com/shanreed25/Python-Cheatsheet/tree/main/DataStructures/Dictionaries)

