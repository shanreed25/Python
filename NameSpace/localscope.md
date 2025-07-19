# Local Scope
- created when a function or method is called
- contains the names defined within that specific function or method
  - these names include function, variables, lists etc....
- when a function finishes execution, its local namespace is typically destroyed.
- if you try to use something that is in local scope, in global scope you will get a `NameError`

## Functions :
- Functions and methods create their own local namespaces for variables and parameters defined within them
```
# Local Scope Variable
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()# returns 2

# Can't access this potion_strength outside its local scope
print(potion_strength)# NameError: name 'potion_strength' is not defined
```

# Enclosing function
- In the case of nested functions, the inner function can access names from the enclosing function's namespace 
  - if those names are not defined locally within the inner function
- sometimes referred to as the "enclosing function local" namespace
```
player_health = 10
def game():#enclosing function
    def drink_another_potion():#inner function
        print(player_health)

    drink_another_potion()


# Can't access this drink_another_potion function outside
# its local scope which is the game function
drink_another_potion()#NameError: name 'drink_another_potion' is not defined
```