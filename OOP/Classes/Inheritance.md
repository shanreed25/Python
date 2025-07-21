# Class Inheritance
**Is the process of inheriting behavior and appearance from and existing class is known as**
- allows a new class (child or subclass) to derive attributes and methods from an existing class (parent or superclass)
- promotes code reusability, extensibility, and a clear hierarchical organization of code
- can inherit both appearence(attributes) and behavior(methods)

# Parent Class (Superclass):
- class from which other classes inherit. It defines common attributes and methods shared by its subclasses.
# Child Class (Subclass):
- class that inherits from a parent class. It can access and utilize the parent's attributes and methods, and can also add its own unique attributes and methods, or even override inherited ones.
# is-a Relationship:
- inheritance represents an "is-a" relationship, meaning a child class "is a type of" the parent class (e.g., a "Dog is an Animal").
# super() function:
- a built-in function is used within a child class to call methods of the parent class, especially useful for initializing parent class attributes in the child's __init__ method.
# Method Overriding:
- a child class can define a method with the same name as a method in its parent class. When this happens, the child class's method will be executed instead of the parent's when called on an instance of the child class


# Types of Inheritance: Python supports several types of inheritance
- **Single Inheritance:** A child class inherits from only one parent class.
- **Multiple Inheritance:** A child class inherits from more than one parent class.
- **Multilevel Inheritance:** A child class inherits from a parent class, which itself inherits from another class, forming a chain.
- **Hierarchical Inheritance:** Multiple child classes inherit from a single parent class.
- **Hybrid Inheritance:** A combination of two or more of the above types.


# Benefits of Inheritance
- **Code Reusability**
    - Avoids duplicating code by defining common functionalities in a parent class and reusing them in multiple child classes.
- **Extensibility**
    - Allows for easy addition of new features or specialized classes without modifying existing code.
- **Maintainability**
    - Centralizes common logic, making code easier to manage and update.
- **Polymorphism**
    - Enables objects of different classes to be treated as objects of a common type, allowing for flexible and generic code

________________________________________________________

```
class Car:# super class
    def __init__(self):
        self.num_of_tires = 2
    def drive(self):
        print("VOOOMMM!!!!!")
class Honda(Car):
    # allows us to inherit everything that the Car class has
    def __init__(self):
        # The Car's init method: refers to the super class Car
        super().__init__()# the call to super in the initialiser is recommended, but not strictly required
        self.num_of_tires = 2 # overrides the num_of_tries in super class  class

    def drive(self):
        super().drive()# do everything that the drive method from the super class does
        # extending the functionality of the drive method
        print("driving very slow")# an also do this

    def self_drive(self):
        print("Driving it's self")

red_car = Honda()
red_car.self_drive()
red_car.drive()
print(red_car.num_tires)

```
