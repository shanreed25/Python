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
- while there is only one type of dictionary comprehension, it can be used in various forms or applications depending on the desired outcome
## Dictionary Comprehension Basic Syntax

- `new_dict = {key_expression: value_expression for item in iterable}`
- **key_expression:** an expression that determines the key for each item in the new dictionary.
- **value_expression:** an expression that determines the value for each item in the new dictionary.
- **item:** a variable that represents each element from the iterable during the iteration.
- **iterable:** the source collection (e.g., list, tuple, set, another dictionary's items(), keys(), or values()) from which the items are processed

## Conditional filtering
- an if statement can be added to include only specific items based on a condition
- `new_dict = {key_expression: value_expression for item in iterable if condition}`

## Conditional value assignment
- an if/else expression can be used within the value_expression to assign different values based on a condition
- `new_dict = {key: (value_if_true if condition else value_if_false) for item in iterable}`
- Keyword Method: 

## Basic Dictionary Creation
- **Create a new dictionary from an iterable**
    - **Keyword Method:** `{new_key: new_value for item in list}`
        - create a new dictionary with the `new_key` and `new_value` for `items` in the` iterable`
- **Example: For each name in the list generate random score and create a dictionary from it**
    ```
    names_list = ["Tatum", "Clayton", "Reed", "James", "Shannon", "Ace", "Mike", "Jane", "Will", "Lisa"]
    score_dict = {name: random.randint(75, 100) for name in names_list}
    print(score_dict)
    ```
- **Example: Create a dictionary that takes each word in the given sentence and calculates the number of letters in each word**
    ```
    sentence = "Do you want to receive updates on live and upcoming series?"
    # sentence.split(" "): splits the sentence by spaces
    word_dict = {item: len(item) for item in sentence.split(" ")}
    print(word_dict)# returns {'Do': 2, 'you': 3, 'want': 4, 'to': 2, 'receive': 7, 'updates': 7, 'on': 2, 'live': 4, 'and': 3, 'upcoming': 8, 'series?': 7}
    ```

    - Using Regular Expressions: `import re`
        ```
        # If we want to split a sentence more flexibly, like ignoring punctuation marks, we can use the re module
        # Split the sentence using regex to keep only words
        fa_word_dict = {item: len(item) for item in re.findall(r'\b\w+\b', sentence)}
        print(fa_word_dict)# {'Do': 2, 'you': 3, 'want': 4, 'to': 2, 'receive': 7, 'updates': 7, 'on': 2, 'live': 4, 'and': 3, 'upcoming': 8, 'series': 6}

        ```

        ```
        # Split the sentence by spaces and question marks
        re_word_dict = {item: len(item) for item in re.split(r'[ ?]+', sentence)}
        print(re_word_dict)# {'Do': 2, 'you': 3, 'want': 4, 'to': 2, 'receive': 7, 'updates': 7, 'on': 2, 'live': 4, 'and': 3, 'upcoming': 8, 'series': 6, '': 0}
        ```


_________________________________________________________________

## Transforming an existing dictionary 
- **Create a new dictionary based on values in an existing dictionary**
    - **Keyword Method:** `{new_key: new_value for (key, value) in dict.items()}`
        - get hold of all the items in the dictionary `dict.items()`
        - then split it into a key and value `(key, value)`
        - then use the `(key, value)` to create a new dictionary with the `new_key: new_value`
- **Example: Create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit**
    ```
    weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

    weather_f = {weekday: (c_degree * 9/5) + 32 for (weekday, c_degree) in weather_c.items()}

    print(weather_f)# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
    ```
___________________________________________________________________

## Filtering with if clauses
- **Create a new dictionary based on values in an existing dictionary, if a condition is true**
    - **Keyword Method:** `{new_key: new_value for (key, value) in dict.items()n if test}`
        - get hold of all the items in the dictionary `dict.items()`
        - then split it into a key and value `(key, value)`
        - if `if test` is true
        - then use the `(key, value)` to create a new dictionary with the `new_key: new_value`
- **Example: Loop through the dictionary and get every person who has a score of 90 and above and add their name(key) and score(value) to the new dictionary**
    ```
    score_dict = {'Tatum': 75, 'Clayton': 83, 'Reed': 75, 'James': 92, 'Shannon': 78, 'Ace': 100, 'Mike': 90, 'Jane': 92, 'Will': 84, 'Lisa': 79}
    a_students = {name: score for (name, score) in score_dict.items() if score >= 90}
    print(a_students)# returns {'James': 92, 'Ace': 100, 'Mike': 90, 'Jane': 92}
    ```

## Nested dictionary comprehension
___________________________________________________________________


## Using functions within comprehension
___________________________________________________________________


