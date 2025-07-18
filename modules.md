# Importing modules
- Import entire Module: `import modulename`
    - if you are only using it once or twice
    - `import random`
    - `random.choice([1, 2, 3, 4])`:
- Import modules and give it a alias: `import modulename as alias`
    - `import random as r`
    - `r.choice([1, 2, 3, 4])`
- Import certain things from modules: `from modelename import aThingInModule, anotherThingInModule`
    - if you are using something more than three times
    - `from random import choice`
    - `choice([1, 2, 3, 4])`

- Import Everything: `from modelename import *`
    - this can make it hard to know when things come from, so you should avoid importing this way
    - `import random *`
    - `choice([1, 2, 3, 4])`: this can be confusing because you cannot tell where choice comes from right away

# Installing Modules
- there are some modules that you cannot just import
- some modules are packaged with the Python standard library
    - random, turtle etc.....
    - Python standard library is a small library of code which contains just the basics to get you started
- there is a much bigger library than the Python standard library
    - this library is the Python packages which are hosted on the internet
    - we need to install these packages into our projects when we need them


# Python Packages
- A directory (folder) that contains one or more modules, and an __init__.py file (which can be empty). 
  - The __init__.py file signifies that the directory is a Python package and not just a regular folder. 
  - a modules is a single Python file (with a .py extension) containing code like functions, classes, and variables
- are a way of organizing related modules into a directory structure, similar to folders containing files
- provide a hierarchical way to structure code, making it easier to manage and reuse code across different projects
- are a fundamental part of Python's code organization and are used extensively in both small and large projects. 

# Python Package Index
- the official third-party software repository for Python
- a central hub where Python developers can share and find packages, modules, and tools for their projects
- think of it as the "App Store" for Python, where you can find and install a vast array of pre-built solutions
- a bunch of software for the python language that is developed and shared by the python community 
- Here's a more detailed breakdown:
What it is:
PyPI is a website (pypi.org) and a database that stores metadata about Python packages, along with the package files themselves. 
Why it's important:
It simplifies the process of finding and installing libraries, saving developers time and effort by providing access to a massive collection of pre-built code. 
How to use it:
Python's package installer, pip, uses PyPI as its default source for downloading and installing packages. You can use pip install <package_name> in your terminal to install packages from PyPI. 


# Purpose of Packages:
- Organization
    - Packages allow you to group related modules together, making your codebase more organized and easier to navigate 
- Reusability
  - You can reuse modules within a package across different projects by importing the package
- Namespacing
  - Packages help avoid naming conflicts between modules by providing a hierarchical namespace
  - For example, you can have package1.moduleA and package2.moduleA without confusion
- Distribution
  - Packages can be bundled and distributed as a single unit, making it easier to share your code with others

# How to Use Packages
1. Install it (if it's not part of the Python standard library)
   - Windows: File --> Settings --> Project name --> Python Interpreter --> Click `+`, search for the package and click install
   - to install any package that you find in the python package index
   - See the source Code: after import, right-click the name of the package and select Go To ---> Implementation
2. Import the package or its modules using the import statement


# Where do packages go
- when you install a package it gets installed into the local virtual environment
- the local virtual environment, is on a per project basis
- inside the `.venv` folder, which usually get created for you

# Why Virtual Environments
- first came Python 2 then cam Python 3
- Python 3 is not backwards compatible with Python 2
- So if you code that is written in Python 2 and you try to add Python 3 to that project it will not work
- So you have to make a choice to use Python 2 or 3, but you cnnot use both
- some modules work for Python 3 but not Python 2
    - so virtual environments defines a small sandbox for each project
    - so we know that our modules are compatible and works with all of the other packages that we install
    - its like the project is frozen in time, so when it is compiled it works as expected even if Python or modules changes versions
- you can use `pip` to install packages but, you may install it in the wrong place, and you project will not be able to access them outside the sandbox
- You want to use PYcharm to handle and install modules
    - this will ensure that it works with the rest of the virtual environment
    - ensures that there are no erros that occur when installed
    - the version used in maintained