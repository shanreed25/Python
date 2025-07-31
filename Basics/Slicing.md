# Slicing
- a powerful and concise method for extracting specific portions of sequences, such as strings, lists, or tuples
- allows for the creation of new sequences containing a subset of elements from the original

- `sequence[start:stop:step]`
    - **start (optional):** starting index of the slice (inclusive). If omitted, it defaults to the beginning of the sequence (index 0).
    - **stop (optional):** **ending index of the slice (exclusive). The element at this index is not included in the slice. If omitted, it defaults to the end of the sequence.
    - **step (optional):** increment between elements in the slice. If omitted, it defaults to 1. A negative step can be used to slice in reverse order.

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
- get elements from index 4 up to (but not including) index 8
    - `my_list[4:8]`: returns [50, 60, 70, 80]
- get elements from the beginning to a specific index
    - `my_list[:3]` returns [10, 20, 30]
- get elements from a specific index to the end
    - `my_list[5:]` returns [60, 70, 80, 90, 100]
- get every 3rd number from a specific index(0) to specific index(6)
    - `my_list[0:6:3]` retuens [10, 40]
- get every 2nd element
    - `my_list[::2]` [10, 30, 50, 70, 90]
- get every 3rd element
    - `my_list[::3]` [10, 40, 70, 100]
- reverse slicing
    - `my_list[::-1]` returns [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
- slicing from end
    - `my_list[-3:]` returns [80, 90, 100]

# my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
- get elements from index 1 up to (but not including) index 3
    - `my_tuple[1:3]` returns (20, 30)
# my_string = "Hello, From Python!"
- get elements from the beginning to a specific index
    - `my_string[:3]` returns 'Hel'


# Key Points:
- Python sequences are 0-indexed.
- The stop index in a slice is always exclusive.
- Slicing creates a new sequence; it does not modify the original.
- Out-of-bound indices in slicing do not raise errors; Python simply returns the available elements within the specified range.