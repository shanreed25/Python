# Classes

# Python: Object Orientd Programming
- model real life objects and those objects have things and can do things
- they have `attributes`, which are modeled with variables
- they can do `methods`, which are modeled with functions
- a model is a way of combining some piece of data and some functionality together

# Model Object: Babysitter
- attributes: what it has
  - attribute is a variable that is associated with a modeled object
  - attributes are attached to a particular object
  - `is_holding_baby = True`
  - `kids_to_handle = ["Ricky", "Molly", "Tai"]`
- methods: what it does
  - methods are functions that a particular modeled object can do
  - methods are attached to a particular object
  - ```
    def cook(ingredients, stove):
        # code to cook food
    ```
  - ```
    def feed_kids(table, chairs, food, kids):
        # code to feed kids
    ```
- So, the babysitter object
  - have a `is_holding_baby` and `kids_to_handle` attribute/variable
  - can `cook()` and `feed_kids()`

# Class vs Object
- multiple objects can be generated from the same type
  - Example: we can generate multiple babysitters from the same model/blueprint
- In OOP this model/blueprint/type is called a `class`
  - and every object we create from the `class` is called `object`
    - so we can generate a new babysitter `object` from the babysitter `class`
- `lisa = Babysitter()`: lisa is the object that is being created from the BabysitterBlueprint() class
  - `lisa` is a variable that contains the `Babysitter()` object 
    - the variable name can be anything
  -  `BabysitterBlueprint()` is the class
    - written with the first letter of each word capitalized(pascal case)
    - `()` activates the construction of the object from the class
# Classes



# Create a class
- `class Babysitter:`
- written with the first letter of each word capitalized(pascal case)

# Using a class to create an object
- `()`: used to initialize/construct an object from a class


# Adding Attributes 
- object attributes can be created and assigned values using dot notation in a few different ways
- Dynamically After Object Creation
  - `sitter_1 = Babysitter()`
  - add attribute f_name: `sitter_1.f_name = "lisa"`
  - add attribute l_name: `sitter_1.l_name = "gram"`
  - add attribute phone_number: `sitter_1.phone_number = "1234567890"`
- Within a Class Definition (Instance Attributes)
  - Attributes are typically defined within the __init__ method of a class, which is the constructor
  - known as instance attributes, as each instance of the class will have its own copy of these attributes
- Class Attributes
  - Attributes can also be defined directly within the class body, outside any methods
  - are class attributes, and they are shared by all instances of the class
- Using `setattr()`
  - The built-in setattr() function provides another way to set an attribute on an object
  - useful when the attribute name is determined at runtime.