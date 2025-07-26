# Dictionaries
Dictionaries allow us to group together and tag related pieces of information, and functions similarly to a dictionary in real life. 
It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.
- Every dictionary has two parts
  - Key: equivalent of a word, in a real life dictionary
  - Value: equivalent of the definition of a word, in a real life dictionary
`emp_phone_numbers = {"Lisa": 123-456-7890}`
## Key
- must be the correct data type
  - emp_phone_numbers = {Lisa: 123-456-7890}
  - Python thinks that Lisa is variable you declared somewhere
  - will cause a: `NameError: name 'Lisa' is not defined.`

## Value

##  Create Empty Dictionary
- `emp_phone_numbers = {}`

## Create Dictionary with content
- `emp_phone_numbers = {"Lisa": 1234567890, "James": 9876540321, "Kim": 5673456288}`

## Retrieve items from a dictionary
- Elements are identified by the Key, and counting starts at 1
- If you try to retrieve, but you spell the key wrong you will get a
  - `KeyError:` which means the key does not exist and cannot be found
  - `emp_phone_numbers["Jmaes"]`
- If you try to retrieve, but you don't use the correct data type you will get a 
  - NameError: name 'James' is not defined
  - `emp_phone_numbers[James]`


## Add new items to an existing dictionary
- `emp_phone_numbers["Mary"] = 5432345678`
- if it finds nothing with that key then it's going to create a new entry with the new key and value

## Edit an item in dictionary
- You edit items in a dictionary the same why you add a new item
- `emp_phone_numbers["Kim"] = 1234565678`
  - will look through the dictionary and find a value with this key
  - then assign it to whatever is on the right side of the equals sign
  - if it finds nothing with that key then it's going to create a new entry with the new key and value


## Remove and return item by index: pop()
- used with lists and dictionaries to remove and return an element
- Dictionary Syntax: `dict.pop(key)`
  - removes the key-value pair associated with the specified key from the dictionary
  - returns the value associated with the removed key
- If the key is not found and no default_value is provided, a `KeyError` will be raised.
- Dictionary Syntax with default value: `dict.pop(key, default_value)`
  - if the key is not found and a default_value is provided, it returns the default_value instead of raising an error.

# Max

```
bids = {
    "Shannon": 215.0,
    "lisa": 124.0,
    "James": 119.0,
    "Molly": 220.0,
    "Mike": 212.0,
}

# Returns the Key of the highest price as the value
max_value = max(bids, key=bids.get)
print(max_value)
```



## Wipe an entire dictionary
- Same way you create a new dictionary: `emp_phone_numbers = {}`
__________________________________________________________

- [Loop through a dictionary](./docs/loop.md)
- [Dictionary Comprehensions](./docs/DictionaryComprehension.md)





_____________________________________

