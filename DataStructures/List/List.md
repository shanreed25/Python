# Python Lists: https://docs.python.org/3/tutorial/datastructures.html
Built-in data type used to store an ordered collection of items
- Python list are ordered so, items in a list maintain a specific order
- The order does not change unless explicitly modified
- Index start at 0
- -1 will access the last item in the list
- Created and searched using square brackets[]
- Python list are changeable (mutable) and they allow duplicates 

##  Create Empty List
- `southern_states = []`

## Create List with items
- `southern_states = ["Florida", "Georgia", "Alabama", "Louisiana", "Mississippi"]`

## Check if an element is present within a list
  - **in operator**: `if item in my_list:`

## Retrieve items from a List
- `southern_states[1]`: will return "Georgia"
- `southern_states[2]`: will return "Alabama"
- When you try to access an item that is not in the range of the List, you will get an IndexError.
  - `southern_states[10]`: This will be an IndexError

## Add new items to an existing List: .append()
- you can append a single item or a list
- `southern_states.append("Tennessee")`
  - will add item to the end of the list
- `southern_states.append(["LongLand", "New Mile", "Bandland"])`
  - will add many items to the end of the list


## Add list to list: .extend(): +=
- you can extend a list with another list, but not a single item
- `southern_states.extend(["Tennessee", "Kentucky", "South Carolina"])`
  - same as `southern_states += ["Tennessee", "Kentucky", "South Carolina"]`
- `southern_states += "Tennessee"`: this may not give you the result you expect
  - will give you: 
    - `['Florida', 'Georgia', 'Alabama', 'Louisiana', 'Mississippi', 'T', 'e', 'n', 'n', 'e', 's', 's', 'e', 'e']`
    - it iterates over each character and adds each character as a item in the list
    - instead the item can be placed in a list to append: `southern_states += ["Tennessee"]`
- `num_list = [3, 6, 9]`
  - `num_list += 3`: will return error `TypeError: 'int' object is not iterable`
  - because it is trying to iterate over something, but you cannot iterate over a single item
  - instead the item can be placed in a list to append: `num_list += [3]`

## Delete Items from a list : .remove()
- removes only the first occurrence of a specified value
- modifies the list in-place, meaning it doesn't return a new list, but rather alters the existing one
- if the value is not found in the list, it raises a `ValueError`
- Syntax: `list.remove(value)`


## Remove and return item by index: pop()
- used with lists and dictionaries to remove and return an element
- List Syntax: `list.pop(index)`
  - removes and returns the element at the specified index
  - if no index is provided, `pop()` removes and returns the last element of the list
  - if the provided index is out of range, a `IndexError` will be raised.
- del statement, or list comprehensions might be more suitable

## Modify Items in a list
- You can modify list after creation
  - `southern_states[2] = "Bama"`
    - changes the value of item at specific position

## Nested list
- list inside other list also called 2D List
```
fruits = ["Strawberries", "Grapes", "Peaches"]
vegetables= ["Potatoes", "Kale", "Spinach", "Tomatoes"]

fruits_vegetables = [fruits, vegetables]
```
- The list would look like this: 
```
[["Strawberries", "Grapes", "Peaches"], ["Potatoes", "Kale", "Spinach", "Tomatoes"]]
```

- Access items
  - `fruits_vegetables[1][1]`: will return "Kale"


__________________________________________________________

- [List Comprehensions](./docs/Listcomprehension.md)