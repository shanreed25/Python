# time
- represents a time of day (hour, minute, second, microsecond)

### Creating time objects
- Passing no arguments: `time = time()` returns 00:00:00
- Passing arguments: `time(hour=3, minute=10, second=5, microsecond=4)` returns 03:10:05.000004
- current time: `now.time()`


### Accessing time components
- you can access hour, minute, seconds
- `time(3, 10, 5, 4).minute`
- `time(3, 10, 5, 4)..hour`

________________________________________________________________________________________________________________

### Formatting time objects
- To format a time object into a string, you can use the strftime() method with format codes

#### Common strftime format codes for time:
- **%H**: Hour (24-hour clock) as a zero-padded decimal number (00-23)
- **%I**: Hour (12-hour clock) as a zero-padded decimal number (01-12)
- **%M**: Minute as a zero-padded decimal number (00-59)
- **%S**: Second as a zero-padded decimal number (00-59)
- **%p**: Locale's equivalent of AM or PM
- **%f**: Microseconds as a decimal number (000000-999999)