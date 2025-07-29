


# How widget work
- Tkinter uses arbitrary keyword arguments for a lot of the Methods properties or initializing Components
    - arbitrary keyword arguments(**kwargs), are collected into a dictionary
    - You can learn more about arbitrary keyword arguments [here](../../../Functions/docs/CustomizedFunctions.md#unlimitedarbitrary-keyword-arguments--kwargs)
- we can set these options in a number of ways
    1. When the object is initialize
        - `my_Label = Label(text="I am a label", font=("Arial", 24, "bold"))`
    2. Like they are keys in a dictionary, then set the value, this can also update text
        - `my_label["text"] = "I am a label"`
        - `my_label["font"] = (text="I am a label", font=("Arial", 12, "bold")`
    3. Using the config() method, this can also update text
        - `my_label.config(text="I am a label", font=("Arial", 24, "bold"))`


# END
- a constant, defined within the tkinter module, that is used primarily with text-based widgets like Text and Entry
- it refers to the position immediately after the last character of the content within that widget
- a convenient way to specify the end of the text without needing to calculate the exact character index
- `END` represents the position after the last character, in some contexts, particularly with Text widgets, it might refer to the newline character that is implicitly present at the end of the text
    - to refer to the position before the final newline, you might use expressions like "end -1c"

## Key uses of END:
- **Retrieving all text**
    - When using methods like get() on Text or Entry widgets, `END` can be used as the second argument to retrieve all content from a starting point to the very end
    - `text_widget.get("1.0", tk.END)` retrieves all text from the beginning of the Text widget
    - `1.0` means getting hold of the text starting from the firstline at the character 0
- **Inserting text at the end**
    - When using the insert() method, END can be used as the index to append new text to the existing content. For example, entry_widget.insert(tk.END, "New text") adds "New text" at the end of the Entry widget.
- **Deleting text up to the end**
    - Similarly, with the delete() method, END can be used to specify the end of the range to be deleted. For example, entry_widget.delete(0, tk.END) clears all content from an Entry widget.


_______________________________________