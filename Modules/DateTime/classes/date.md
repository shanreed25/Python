# date class
- represents a calendar date(year, month, day) without any time information

### Creating date objects 
- date instances can be created by passing require arguments to its constructor
    - Syntax: `date(year=2003, month=5, day=25)` or `date(2003, 5, 25)` returns 2003-05-25
- get current date: `date.today()`

### Accessing date components
- you can access the year, month, and day attributes of a date object
    - year: `date(2003, 5, 25).year` returns year as integer
    - month: `date.today().month` retuns the month as a integer
    - day: `date(2003, 5, 25).day` retuens day as integer

________________________________________________________________________________________________________________

# date methods
- `date.today()` returns the current date ex. 2008-09-09



### Formatting date objects into strings
- use the `strftime()` method to format a date object into a string with a specified format
- "strftime" stands for "string format time