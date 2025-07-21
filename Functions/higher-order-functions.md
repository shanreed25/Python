# Higher-order functions
- functions can work with other functions
- it can take one or more functions as arguments
- return a function as their result

The concept of higher-order functions is closely related to "first-class functions," which means that functions are treated as first-class objects in Python. This implies that functions can be: Assigned to variables, Passed as arguments to other functions, Returned as values from other functions, and Stored in data structures like lists or dictionaries.
Higher-order functions are a key element of functional programming paradigms, promoting code that is more concise, readable, and often more robust by reducing side effects and promoting immutability. Decorators in Python are a common and powerful application of higher-order functions.


# Functions As Arguments
- allows for flexible and reusable code
- the behavior of the higher-order function can be customized by the function(s) passed to it
- useful when you want to listen for events then trigger another function
- Examples include `map()`, `filter()`, and `sorted()`
- it is recommended that when using higher order functions or methods that you have not created yourself
  - you should use keyword arguments instead of positional arguments
  - especially if the position does not have any meaning: `screen.onkey(fun=move_forward, key="space")`

# Function as a Result
- enables creating functions dynamically or building decorators