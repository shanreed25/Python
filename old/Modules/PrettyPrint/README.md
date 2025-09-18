# Pretty Print
- the process of displaying complex data structures, such as nested lists, dictionaries, or custom objects, in a well-formatted and human-readable way
- when you use the standard print() function on a complex data structure, especially one with multiple levels of nesting, the output can be a single, long, and difficult-to-read line
-  useful during debugging and development, as it helps in quickly understanding and visualizing the contents of complex data structures


### What Pretty Print Does
- **Indentation**: Adding appropriate indentation to clearly show the hierarchical structure of nested elements
- **Line breaks**: Inserting line breaks to prevent excessively long lines and improve readability
- **Formatting options**: Providing options to control aspects like output width, dictionary key sorting, and the depth of nested structures to be displayed


### How to use
- pprint.PrettyPrinter objects (`pprint.pprint()`) offers several parameters to fine-tune the output
    - **indent**: Specifies the amount of indentation for each nesting level.
    - **width**: Sets the desired maximum number of characters per line.
    - **depth**: Limits the number of nesting levels to be printed.
    - **sort_dicts**: Controls whether dictionary keys are sorted alphabetically


**Tip: you can reassign print = pprint.pp for use within a scope**

[More](https://docs.python.org/3/library/pprint.html#functions)