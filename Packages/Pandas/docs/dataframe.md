# Data Frame
- a two-dimensional labeled data structure with columns of potentially different types, analogous to a spreadsheet or a SQL table

# Two Dimensional(2D) Data Object
- data arranged in a grid or table, with rows and columns
    - two axis of organization, allowing for relationships between data points in both directions
- can be visualized as a excel table/sheet
- often represented as a matrix or a data frame in programming
- access data in a 2D data object requires two indices (e.g., my_datax[3][6]) to access a specific element

# Create a Data Frame 
- you can use `pandas.DataFrame()` to create a Data Frame

**From a Dictionary**
```
data_dict = {
    "students": ["James", "Lisa", "Rita", "Keon", "Rider"],
    "scores": [89, 76, 82, 100, 73]
}
my_data = pandas.DataFrame(data_dict)

# Convert Data to CSV File
my_data
```
- You can also create a Data frame from
    - From a List of Dictionaries
    - From a List of Lists (with optional column names)
    - Empty DataFrame
    - Data Consistency: When creating a DataFrame from a dictionary of lists, ensure all lists have the same length to avoid errors

# Accessing Data in a Data Frame
- `data = pandas.read_csv("path to file")` returns a data frame
- `to_dict()` converts the data to a dictionary
    - `data.to_dict()`

# DataFrame from a list
the pd.DataFrame() constructor is utilized. This method offers flexibility in handling various list structures. 
1. From a single list (as a single column):
2. From a list of lists (where each inner list represents a row):
3. From multiple lists (zipped together to form columns):