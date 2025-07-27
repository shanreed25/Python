# Customizing Functions
- you can customized functions by providing parameters


# Benefits of using parameters
- **Reusability:** Functions can be used with different data inputs without modifying the function's core logic.
- **Flexibility:** Parameters allow for dynamic behavior and customization of the function's actions.
- **Modularity:** They promote cleaner code by encapsulating specific operations and their required inputs.
- **Clarity:** Parameters make the function's purpose and expected inputs clear to anyone reading the code.



# Default Parameters
- when one or more parameters are assigned a default values, in the function definition
- allows the function to be called without explicitly providing an argument for that parameter, arguments are optional for that parameter
- if an argument is not provided during the function call, the default value is used
- if an argument is provided during the function call, it overrides the default value
- parameters with default values must be placed after all non-default parameters in the function signature
    - `def func_name(param1, param2=default_value)`


# Unlimited(Arbitrary) Arguments
- an arbitrary or "unlimited" number of arguments
- utilize special syntax
    - `*args` for non-keyword arguments
    - `**kwargs` for keyword arguments
- The names `args` and `kwargs` are conventions; any valid variable name can be used after the `*` and `**`
- These arbitrary argument types can be combined with regular positional and keyword arguments in a function definition, following a specific order: regular arguments, *args, regular keyword arguments, **kwargs

## Unlimited(Arbitrary) Positional Arguments (*args)
- an asterisk `*` before a parameter name allows the function to accept any number of **positional arguments**
- the arguments are collected into a tuple within the function, accessible via the specified parameter name
    - `def add(*args):` you would use `args` to access the values
- these are called positional arguments because the arguments are passed based on their position in the function call
    - so when you call the function, the first argument provided will be the first element in the args tuple
        - can be accessed by index: `args[0]`

- **Example `*args`:**
```
    def add(*args):
        #access by index
        print(args[0]) # 1

        my_args_sum = 0
        # loop through
        for num in args:
            my_args_sum += num
        return my_args_sum

print(add(1, 3, 5, 7, 9))# 25
```



## Unlimited(Arbitrary) Keyword Arguments (`: kwargs`)**:
- a double asterisk `**` before a parameter name allows the function to accept any number of **keyword arguments**
- the arguments are collected into a dictionary within the function, where keys are the argument names and values are their corresponding values
     - `def add(**kwargs):` you would use `kwargs` to access the values
- these are called keyword arguments because
- **Example `kwargs`:**
```
    def calculate(**kwargs):
        print(kwargs)# {'add': 5, 'multiply': 10, 'divide': 2}
        for key, value in kwargs.items():
            print(key)
            print(value)
        print(kwargs["add"]) # 5

    calculate(add=5, multiply=10, divide=2)
```

- Learn how to use unlimited positional and keyword aruguments with classes [here](../../OOP/Classes/Classes.md)



# def add(*args):
#     #access by index
#     print(args[0])
#     my_args_sum = 0
#     # loop through
#     for num in args:
#         my_args_sum += num
#     return my_args_sum
#
# # print(add(1, 3, 5, 7, 9))
#
#
# def calculate(**kwargs):
#     print(kwargs)# {'add': 5, 'multiply': 10, 'divide': 2}
#     for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#         pass
#     print(kwargs["add"]) # 5
#
#     # Dictionaries
#     # we can also use a function called get()
#     # pass in the name of the key if we want to get hold of the value
#     # benefit is that if the ksy does not exist in the dictionary, it will return none, instead of giving a KeyError
#     print(kwargs.get("divide"))  # 2
#
# calculate(add=5, multiply=10, divide=2)
