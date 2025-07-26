# Looping through a Data Frame
- you can loop through Data frame in the same way that you loop through a dictionary
    - because a Data Frame is like a Python Dictionary

- Dictionary
```
student_dict = {
    "students": ["James", "Lisa", "Rita", "Keon", "Rider"],
    "scores": [89, 76, 82, 100, 73]
}
```

- Create a Data Frame from a dictionary
    - `student_data_frame = pandas.DataFrame(student_dict)`

- Loop through data frame using `items()`
    ```
    for (key, value) in student_data_frame.items():
            print(key)# returns column names
            print(value)# returns data in each column
    ```
    - not really useful because its basically just looping through the names of the columns and the data inside each of the columns
    - instead you can use pandas built-in loop: a method called `iterrows()`


- Loop through data frame using `iterrows()`

    ```
    for (index, row) in student_data_frame.iterrows():
    # index is the number in the first column of a data frame
        print(index)# prints each row index
        print(row)# prints each row of data

        print(row["student"])# prints each student name value
        print(row.student)# prints each student name value


    ```
    - **iterrows():** allows us to loop through each of the rows of the a data frame
    - each row is a Pandas Data Series Object
    - we can get access to the row values through its columns/attributes using dot or bracket notation
    - Dictionary Comprehension Keyword Method with iterrows()
        `{new_key:new_value for (index, row) in df.iterrows()}`