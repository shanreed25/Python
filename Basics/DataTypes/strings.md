# String Methods

#### `strip()`
- used to remove specified characters from the beginning and end (leading and trailing) of a string
- `string.strip()`: removes leading and trailing whitespace characters by default
    - whitespace characters include spaces, tabs (\t), newlines (\n), carriage returns (\r), form feeds (\f), and vertical tabs (\v)
- returns a new string with the characters removed, leaving the original string unchanged
- **chars (optional):** A string specifying the set of characters to be removed
    - `string.strip("#")`: remove specific characters
    - `string.strip(".-* ")`: removing multiple specific characters
    - order of characters does not affect the stripping process
    - removes from both ends of the string until it encounters a character not in the specified set
    - does not remove characters from the middle of the string
        