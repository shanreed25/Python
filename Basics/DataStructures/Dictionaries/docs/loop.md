# Looping through Dictionaires
- Dictionary
```
student_dict = {
    "students": ["James", "Lisa", "Rita", "Keon", "Rider"],
    "scores": [89, 76, 82, 100, 73]
}
```
- **Iterate through a dictionary print the key and value**
    ```
    for key in student_dict:
        print(student_dict[key])
    ```
    - prints
    ```
    ['James', 'Lisa', 'Rita', 'Keon', 'Rider']
    [89, 76, 82, 100, 73]
    ```


- **Iterate through the key-value pairs of a dictionary**
    ```
    for (key, value) in student_dict.items():
        print(key, value)

    ```
    - prints
    ```
    students ['James', 'Lisa', 'Rita', 'Keon', 'Rider']
    scores [89, 76, 82, 100, 73]
    ```

- `for (key, value) in student_dict.items()` and `for key, value in student_dict.items()` have the exact same functionality
- `for (key, value) in student_dict.items():` adds unnecessary parentheses and is less common in modern Python code
- `for key, value in student_dict.items():` the preferred and idiomatic way: in current Python versions (Python 3 and later) due to its conciseness and clarity