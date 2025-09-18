# strftime()
-  method used to format datetime objects into human-readable strings
- a function available for datetime, date, and time objects within the datetime module
- used to convert these objects into a formatted string representation
- `strftime` stands for **string format time**
- provides a flexible way to customize the string representation of date and time objects in Python, making it useful for display, logging, and data formatting purposes


#### How It Works
1. Takes a datetime object and a format string as arguments
    - format string contains standard format codes preceded by a % sign
    - these codes represent different components of the date and time, such as year, month, day, hour, minute, second, and more
    - it replaces these format codes with the corresponding values from the datetime, date, or time object, resulting in a formatted string
2. When strftime() is called, it replaces these format codes with the corresponding values from the datetime, date, or time object, resulting in a formatted string
3. Returns a new string representing the datetime object formatted according to the specified format string

#### Common Format Codes
| Directive   | Description                                                 | Example  |
| :---------- | :---------------------------------------------------------: | -------: |
| %Y          | Year with century                                           | 2022     |
| %y          | Short year without century                                  | 22       |
| %m          | Month as a zero-padded decimal number (01-12)               | 05       |
| %d          | Day of the month as a zero-padded decimal number (01-31)    | 10       |
| %H          | Hour (24-hour clock) as a zero-padded decimal number (00-23)| 14       |
| %M          | Minute as a zero-padded decimal number (00-59)              | 26       |
| %S          | Second as a zero-padded decimal number (00-59)              | 46       |
| %A          | Full weekday name                                           | Friday   |
| %a          | Short weekday name                                          | Fri      |
| %w          | Weekday as a number (0-6)                                   | 0        |
| %B          | Full month name                                             | July     |
| %b          | Short month name                                            | Dec      |
| %p          | AM or PM                                                    | PM       |


 # strptime() 
 - `strptime()` parses strings into datetime objects