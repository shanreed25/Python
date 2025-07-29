# Python: Phases in the execution of a program
- compile-time and runtime refers to different phases in the execution of a program



# Compile-Time
- the phase where the Python interpreter translates your source code (the .py files you write) into an intermediate format called bytecode (stored in .pyc files)
- this bytecode is a low-level, platform-independent representation of your code
- during compile time, the interpreter performs syntax checking, ensuring your code adheres to Python's grammatical rules
    - it identifies and reports syntax errors, such as typos, incorrect indentation, or missing delimiters, before the program even begins to run
- you typically don't directly interact with this compilation step as a Python developer, as it happens automatically when you run or import a Python module

# Run-Time
- the phase where the compiled bytecode is executed by the Python Virtual Machine (PVM)
- the program is actively running, performing its intended operations
- during runtime, the PVM interprets the bytecode instructions and interacts with the operating system and hardware to carry out tasks like memory allocation, variable assignments, function calls, and input/output operations
    - errors that occur during this phase are called runtime errors (or exceptions), such as ZeroDivisionError, TypeError, or NameError, which arise from logical flaws or unexpected conditions encountered during execution.
- this is the phase where you observe the program's behavior, interact with it, and see the results of its execution

___________________________________________________________________________

| Feature | Compile | Runtime |
|---|---|---|
| **Purpose** | Translation of source code to bytecode | Execution of bytecode by the PVM |
| **Errors** | Syntax errors | Runtime errors (exceptions) |
| **Timing** | Before program execution begins | During program execution |
| **Visibility** | Automatic, often unseen by the developer | Direct interaction and observation of results |
