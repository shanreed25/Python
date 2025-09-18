# datetime.timedelta
- represents a duration, or the difference between two datetime
- stores a span of time, not a specific point in time
- timedelta instances can be created by passing appropriate arguments to its constructor


- **Represents a duration** the difference between two datetime or date objects
    - timedelta object stores a span of time, not a specific point in time
    - internally stores days, seconds, and microseconds
    - `datetime.timedelta() # 0:00:00`
    - `datetime.timedelta(days=1) #1 day, 0:00:00`
    - `datetime.timedelta(hours=2) # 2:00:00`

- **Arithmetic operations**
- timedelta objects can be added to or subtracted from datetime or date objects to calculate future or past dates/times(to shift them forward or backward in time)
    - `now = datetime.now()`# Get the current datetime
    - `tomorrow = now + one_day`
    - `in_two_hours = now + two_hours`
- timedelta objects can be added to or subtracted from other timedelta objects, to find the resulting duration
    - `span_a = timedelta(days=1, hours=3) #1 day, 3:00:00`
    - `span_b = timedelta(hours=10) #2:00:00`
    - `total_duration = span_a + span_b #2 days, 5:00:00`