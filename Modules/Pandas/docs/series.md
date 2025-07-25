# Series
- a one-dimensional labeled array capable of holding any data type

# One Dimensional(1D) Data Object
- sequence of data points arranged along a single axis
    - only one axis of organization
- can be visualized as a line, like a list of numbers or a single column in a table or excel sheet
- often represented as a simple array or list in programming
- access data in a 1D data object using a single index (e.g., my_list[8]) to access a specific element

# Accessing Data in a Data Series
```
data = pandas.read_csv("path to file") # returns a Data Frame
```
- Under the hood, Pandas takes each of the columns headings and converts them to attributes
- `data["columnname"]` and `data.columnname` both return a data series
    - `data["columnname"]`: accessing data series like a dictionary, getting each column by the key using bracket notation
    - `data.columnname`: accessing data series like an object, getting each column by attributes using dot notation
- `to_list()` can convert a data series to a list
    - `data["columnname"].to_list()`
    - `data.columnname.to_list()`




# `item()`
**When a Pandas Series contains only one value, using .item() on that Series will directly return the value itself, not a Series containing that value**
- extract the scalar value from a Series that is known to contain only a single element
- provides a direct and efficient way to retrieve the underlying Python scalar, such as an integer, float, or string, without needing to access it through indexing or other methods that might return a Series object
- useful when you have performed an operation that you know will result in a single-element Series
- will raise a ValueError if the Series contains more than one element
- Example:
```
# this is a series that is returned from an operation
0    139
Name: x, dtype: int64

print(series.x.item())# this will return 139
```