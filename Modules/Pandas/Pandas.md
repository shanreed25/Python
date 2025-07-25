# Pandas
- [Docs](https://pandas.pydata.org/docs/)
- [API Reference](https://pandas.pydata.org/docs/reference/index.html)
    - list of all the things you can do with pandas


# Pandas Package
- an open-source software library designed for data manipulation and analysis in Python
- a fundamental tool for data scientists and analysts, built on top of the NumPy library, and provides high-performance, easy-to-use data structures and data analysis tools

# Core features and functionalities of Pandas
- **Core Data Structures:**
    - **[Series](./docs/series.md):** A one-dimensional labeled array capable of holding any data type
    - **[DataFrame](./docs/dataframe.md):** A two-dimensional labeled data structure with columns of potentially different types, analogous to a spreadsheet or a SQL table.
- **Data Handling:**
    - It offers robust tools for handling various data formats, including CSV, Excel, JSON, SQL databases, and more.
- **Data Manipulation:**
    - Pandas provides extensive functionalities for data cleaning, transformation, reshaping, merging, grouping, and aggregation. This includes handling missing data, filtering, sorting, and performing calculations.
- **Time Series Functionality:**
It has powerful tools for working with time series data, including date/time indexing and resampling.
- **Integration:**
    - Pandas integrates seamlessly with other libraries in the Python data science ecosystem, such as NumPy for numerical operations and Matplotlib/Seaborn for data visualization.
**In essence, Pandas simplifies the process of working with structured data in Python, making it an indispensable tool for tasks ranging from data cleaning and preparation to advanced statistical analysis and machine learning pre-processing.**
_________________________________________________________________________________________________________
# How to use Pandas
1. Read CSV File
- `data = pandas.read_csv("path to file")`
    - returns a [Data Frame](./docs/dataframe.md)
- `data["columnname"]` or `data.columnname` returns a [Data Series](./docs/series.md)

- Check out this [file]() and see why pandas is so much better at reading CSV file than Python's file system and the CSV module that comes with python