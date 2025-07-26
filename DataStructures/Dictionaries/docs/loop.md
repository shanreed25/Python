# Looping through Dictionaires
- Dictionary
```
student_dict = {
    "students": ["James", "Lisa", "Rita", "Keon", "Rider"],
    "scores": [89, 76, 82, 100, 73]
}
```
- use for loop to loop through the dictionary print the key and value
    ```
    for key in student_dict:
        print(student_dict[key])
    ```
    - prints
    ```
    ['James', 'Lisa', 'Rita', 'Keon', 'Rider']
    [89, 76, 82, 100, 73]
    ```


- use for loop to loop through the dictionary print the key and value
    ```
    for (key, value) in student_dict.items():
        print(key, value)

    ```
    - prints
    ```
    students ['James', 'Lisa', 'Rita', 'Keon', 'Rider']
    scores [89, 76, 82, 100, 73]
    ```