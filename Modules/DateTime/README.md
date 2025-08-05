# Date Time
- provides classes for working with dates and times
- offers functionalities for representing, manipulating, and formatting date and time information

# Frequently Used Classes
- **[date](./date.md):** to specifically handle dates (year, month, and day)
- **[time]():** to specifically handle time(hour, minute, second, microsecond)
- **[datetime](./datetimeclass.md):** handles both date and time combined 
- **[timedelta]():** represents a duration or the difference between two date, time, or datetime objects.


# Common Operations and Features
- **Creating Objects:**
    - Instances of date, time, and datetime can be created by passing appropriate arguments to their constructors
    - `datetime.date(2025, 7, 31)`
- **Getting Current Date/Time:**
    - Methods like `datetime.now()` or `datetime.today()` retrieve the current local date and time
- **Formatting and Parsing:**
    - **strftime():** Formats a datetime object into a string representation based on specified format codes
    - `%Y-%m-%d %H:%M:%S`
    - **strptime():** Parses a string into a datetime object based on a specified format string
- **Arithmetic Operations:**
    - timedelta objects allow for adding or subtracting durations from date, time, or datetime objects, enabling calculations like finding a date a week from now
- **Extracting Information:**
    - Individual components (year, month, day, hour, minute, etc.) can be extracted as attributes from date, time, and datetime objects.
- **Time Zones:**
    - The datetime module, especially with the zoneinfo module (introduced in Python 3.9), supports handling time zones and daylight saving time.

_______________________________________________________

# datetime methods
- `now()`
- `today()`
- `weekday()`