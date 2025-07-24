# File system
- Python offers robust capabilities for interacting with the file system through various built-in modules and external libraries
- these tools enable operations such as creating, reading, writing, moving, and deleting files and directories, as well as retrieving file and directory information

# Computer file system
- **working directory** is the folder we are currently working from
- **absolute file** path starts from the origin:  `C:\Users\username\PycharmProjects\file-system-info\codeing\learning`
- **relative file**: path starts at the working directory
    - if working directory is `PycharmProjects`
        - then we would use `./file-system-info\codeing\learning`
    - if working directory is `learning` and we want to get to `file-system-info`
        - then we use `../coding/file-system-info`
    - file within the same directory: `./filename.doc` or `filename.doc`

# File Handling
- python's built-in open() function is used for opening files for reading, writing, or appending data
- the with statement is commonly used with open() to ensure proper file closure, even if errors occur.
- `open()`
    - `file = open("my_file.txt")`: takes the file you want to open(as a string)
        - file will open in read only mode
    - the mode you want to open it in, default is read only `mode="r"`
- `read()`
    - `contents = file.read()`: returns the content of the file
- `write()`
    - takes what you want to write to the file
    - you must open the file in write mode: `file = open("my_file.txt", mode='w' )`
    - write to the file: `file.write("I like the color purple")`
        - will delete everything in the file and replace it with what you pass in
    - if you want to add to the file you must change the mode to append
        - `file = open("my_file.txt", mode='a' )`
        - `file.write("\nI like the color purple")`
    - if you try to open a file in write(w) or append(a)  mode and the file does not exist, python will create the file and write to it
- `close()`
    - `file.close()`: closes the open file
    - once python opens a file, it takes up resources on your computer
    - python might at some point close the file and free up those resources
    - but we don't know when or if that will happen
- alternatively to `close()` you can use the `with` keyword to manage the file
    - `with open("my_file.txt") as file:`
        - `contents = file.read()`
    - as soon as `with` notices that we are done with that file it closes the file
    - `file` can be any name you want, its like a variable for the file
    - every thing you want to do with the file goes inside the with block
- `file.readlines()`: Return all lines in the file, as a list where each line is an item in the list object

    - 


# Key Modules for File System Operations:
## os module
- provides a wide range of functions for interacting with the operating system, including file system operations. Examples include:
- **os.mkdir():** Creates a directory.
- **os.remove():** Deletes a file.
- **os.rename():** Renames a file or directory.
- **os.path submodule:** Provides functions for path manipulation, such as os.path.exists(), os.path.isfile(), and os.path.isdir().

## shutil module
- offers high-level file operations, making it easier to perform tasks like copying and moving files and directories recursively.
- **shutil.copy():** Copies a file.
- **shutil.move():** Moves a file or directory.
- **shutil.rmtree():** Deletes a directory and its contents.

# pathlib module (introduced in Python 3.4)
- provides an object-oriented approach to file system paths, offering a more intuitive and readable way to interact with files and directories.
- **Path('my_file.txt').exists():** Checks if a file exists.
- **Path('my_directory').mkdir():** Creates a directory.
- **Path('old_name.txt').rename('new_name.txt'):** Renames a file.


# External Libraries:
**While the standard library covers most common file system needs, external libraries like fsspec and PyFilesystem provide abstractions for working with various storage backends (e.g., cloud storage, FTP servers) in a consistent manner**