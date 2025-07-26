# List Comprehension
- a case where you create a new list from a previous list
    - create new lists by applying an expression to each item in an existing iterable, optionally filtering items based on a condition
- provides a concise and readable way to create new lists based on existing iterables
    - like lists, tuples, range or strings
- offers a more compact syntax compared to traditional for loops with append() operations, often leading to more efficient and elegant code
- **Performance:** Generally, list comprehensions are slightly faster than equivalent for loops that manually append elements to a list, especially for larger datasets. This is because they are optimized at the C level within the Python interpreter and avoid repeated method lookups (like list.append).
    

# List Comprehension Vs For loop
- **For Loop**
    - a general-purpose control flow statement used to iterate over elements of an iterable (e.g., lists, tuples, strings, ranges) and execute a block of code for each element. It can be used for various tasks, including modifying variables, performing side effects, or building complex data structures
    ```
    numbers = [1, 2, 3, 4, 5, 6, 7]
    new_list = []
    for num in numbers:
        add_ten = num + 10
        new_list.append(add_ten)

    print(new_list)
    ```
    - Offers more flexibility for complex logic, multiple operations, or when side effects are intended

- **List Comprehension**
        ```
        numbers = [1, 2, 3, 4, 5, 6, 7]
        new_list = [num + 10 for num in numbers]
        print(new_list)# [11, 12, 13, 14, 15, 16, 17]
        ```
___________________________________________________________________________________________________

# Keyword Method
- when reading a list comprehension it can be hard to understand the structure and flow of the comprehension
- the keyword method helps with understanding  the structure and flow of the comprehension
- the keyword method involves
    1. typing out the list comprehension keywords
    2. then replace each of the words with the actual item in your code
- `[new_item for item in list]`
___________________________________________________________________________________________________

## List from a string 
- Create a list from a string where each letter in the string becomes an item in the list
    ```
    my_name = "Shannon"
    new_name = [letter for letter in my_name ]
    print(new_name)#['S', 'h', 'a', 'n', 'n', 'o', 'n']
    ```
___________________________________________________________________________________________________

## List using range()
```
double_num_list = [num * 2 for num in range(1,5)]
print(double_num_list)
```
___________________________________________________________________________________________________

# Conditional List Comprehension
- **Create a new list containing the expression applied to each item from the iterable, but only if the condition (if present) is True for that item**
    - `[expression for item in iterable if condition]` or `[new_item for item in list if test]`
        - **expression:** represents the value(the result we want for each element) or operation that will be applied to each item to form the new list
            - defines what will be included in the new_list
            - can be a simple item or a modified version of item (e.g., item * 2, item.upper())
        - **for item in iterable:**core iteration part, similar to a for loop
            - **item(for each individual element):** variable name that will sequentially take on the value of each element from the iterable
            - **iterable(in this collection of items):** the source sequence (list, tuple, string, range) that the comprehension will iterate over
        - **if condition (optional):** the filtering part of the comprehension
            - **condition(only if this condition is met):** a boolean expression that determines whether an item should be included in the new list
                - only items for which the condition evaluates to True will be processed by the expression and added to the resulting list
- **Conditional List Comprehension Examples:**
    - Create a new list with the names that have less than 5 characters
        ```
        names_list = ["Tatum", "Clayton", "Reed", "James", "Shannon", "Ace", "Mike", "Jane", "Will", "Lisa"]
        new_names_list = [name for name in names_list if len(name) < 5]
        print(new_names_list)# ['Reed', 'Ace', 'Mike', 'Jane', 'Will', 'Lisa']
        ```
    - Create a new list with the names that have more than 4 characters and change them to all uppercase letters
        ```
        names_list = ["Tatum", "Clayton", "Reed", "James", "Shannon", "Ace", "Mike", "Jane", "Will", "Lisa"]
        upper_list = [name.upper() for name in names_list if len(name) > 4]
        print(upper_list)# ['TATUM', 'CLAYTON', 'JAMES', 'SHANNON']
        ```
___________________________________________________________________________________________________

# New list containing only the elements from a that are not present in b
- **Keyword Method:** `[item for item in a if item not in b]`
    ```
    list_1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
    list_2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
    result = [num for num in list_1 if num in list_2]
    print(result)
    ```
___________________________________________________________________________________________________

# using a dictionary key as new item: Passing in each item from a list as a key to the dictionary
- **Keword Method:** `[new_item for item in list]`
```
my_dict = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot'}
my_list = ['B', 'C', 'D']

dict_values_list = [my_dict[letter] for letter in my_list]
print(dict_values_list)# ['Bravo', 'Charlie', 'Delta']

```