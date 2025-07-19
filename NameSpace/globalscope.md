# Global Scope
- Created when a module is loaded. It contains all the names defined at the module level
- the outermost level of a program or module, where variables defined are accessible throughout the entire program
- variables created in the global scope are called global variables
- Modules: Each module in Python has its own global namespace, preventing name clashes between different modules
- Global variables can be accessed from anywhere within the program, including inside functions and other scopes
  - unless a local variable with the same name shadows them
# Global Scope in .py file
- available anywhere in the file because it was defined at the top level of the file
- top level does not mean at the top of the file it just means it is defined outside a function or method
```
player_health = 10

def drink_new_potion():
        print(player_health)


drink_new_potion()# returns 10

print(player_health)# returns 10
```

# Name Shadow exception
- Global variables can be accessed from anywhere within the program, including inside functions and other scopes
  - unless a local variable with the same name shadows them
```
# global scope variable
dollars = 1


def increase_dollars():
    # local scope variable
    dollars = 2
    # trying to set same variable to 2
    print(f"dollars inside function: {dollars}")

#this refers to the dollars variable in the local scope
increase_dollars() # returns 2
#this refers to the dollars variable in the global scope
print(f"dollars outside function: {dollars}")#returns 1
```

# Global Constants
- variables defined in the global scope that will never get modified or changed
- we should use their values but never need to modify them
- it is convention to use capital letters when creating constants
  - declared in ALL_CAPS with an underscore in between words
- variables in ALL_CAPS helps us remember that it is a constant so that we do not modify it
- `PI = 3.14159`
- `MY_URL = "https://www.mywebsite.com"`