# strftime()
-  method used to format datetime objects into human-readable strings
-  `strftime` stands for **string format time**


#### How It Works
- **Input**: takes a datetime object and a format string as arguments
- **String Formatting**: format string contains a combination of **literal text** and special "format codes" also known as **directives**
    - these codes represent different components of a date and time, such as year, month, day, hour, minute, second, etc
- **Replacement**: replaces the format codes in the format string with the corresponding values from the datetime object
- **Output**: returns a new string representing the datetime object formatted according to the specified format string


 provides methods like strftime() for formatting datetime objects into human-readable strings and strptime() for parsing strings into datetime objects