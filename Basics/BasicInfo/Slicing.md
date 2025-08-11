# Slicing Operation
- a powerful and concise mechanism for extracting specific portions of sequences, such as strings, lists, or tuples
- a fundamental operation that allows for the creation of new sequences containing a subset of elements from the original
- creates a new sequence; it does not modify the original
- `sequence[start:stop:step]`
    - **start (optional):** starting index of the slice (inclusive). If omitted, it defaults to the beginning of the sequence (index 0).
    - **stop (optional):** **ending index of the slice (exclusive). The element at this index is not included in the slice. If omitted, it defaults to the end of the sequence.
    - **step (optional):** increment between elements in the slice. If omitted, it defaults to 1. A negative step can be used to slice in reverse order.

**Slicing using bracket notation is the most common way to perform slicing and is often described as a "method" in a general sense of performing an action on a sequence.However, it's not a method in the object-oriented sense of being a function specifically defined within a class and called on an instance of that class (e.g., my_list.slice()). Instead, it leverages the `__getitem__` special method of the sequence object**

# Slice Objects: `slice()`
- commonly used with the bracket notation `[start:end:step]`, there is also a built-in function called `slice()`
- creates a slice object, which can then be used with the bracket notation to achieve the same result as direct slicing
- allows for more programmatic control over slices, as you can store and reuse slice objects

# Key Points
- Python sequences are 0-indexed
- The stop index in a slice is always exclusive
- Out-of-bound indices in slicing do not raise errors; Python simply returns the available elements within the specified range
- the common bracket notation for slicing relies on the __getitem__ method, rather than being a standalone method named slice on sequence objects
- the `slice()` function is a built-in function that creates slice objects

[Slicing Examples](https://github.com/shanreed25/Python-Cheatsheet/blob/main/Operations/slicing.py)

