# Layout Management
- the process of arranging and positioning widgets (such as buttons, labels, text fields, etc.) within a window 
- dictates how these UI elements are displayed and how they respond to changes in window size or content
- In Tkinter there are three primary layout managers `pack()`, `place()`, and `grid()`



## pack()
- arranges widgets in blocks, packing them against a specified side (top, bottom, left, or right) of their parent container
    - places each widget next to each other, in a logical format
    - by default it will always start from the top then pack every other widget just below the previous one
    - you can change this with the side parameter, Option includes: right, bottom, and left
- it is relatively simple to use for basic layouts but can become less intuitive for complex arrangements
- hard to specify a precise position

## place()
- provides absolute positioning, allowing you to specify the exact x and y coordinates for each widget
- x(left&right) and y(up&down) value for the position
    - Place label in the top left corner: `my_label.place(x=0, y=0)`
- is so specific, and we have to work out in our head where to put each widget
- easy to use with only a few widgets, but figuring out the coordinates for 50 widgets can become a headache to manage
- the most control, it can be less flexible and responsive to window resizing compared to `pack()` or `grid()`

## grid()
- places widgets in a two-dimensional table-like structure, organized into rows and columns
- treats your entire program as a grid
- you can divide it into any number of column and rows you want to
    - Columns are vertical(up and down)
    - Rows are horizontal(left to right)
    - Column and row numbers start at 0
    - put label in the top left corner: `my_label.grid(column=0, row=0)`
- The grid system is relative to other components
    - `my_label.grid(column=5, row=5)`
    - if you only have this one widget then it will be in the top left corner because there are no widgets in columns 1, 2, 3, or 4
- well-suited for creating forms and structured layouts
- you can specify the row and column where a widget should be placed, offering more precise control over arrangement compared to `pack()`
- YOU CANNOT MIX GRID AND PACK IN THE SAME PROGRAM, THIS WILL CAUSE AN ERROR
