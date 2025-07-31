class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            # Menu().menu[2].name = cappuccino
            # Menu().menu[1].ingredients = {'water': 50, 'milk': 0, 'coffee': 18}
            # Menu().menu[0].ingredients["water"] = 200
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]
    # menu()..get_items() = latte/espresso/cappuccino/
    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    # Menu().find_drink("latte").name = latte
    # Menu().find_drink("latte").ingredients = {'water': 200, 'milk': 150, 'coffee': 24}
    # Menu().find_drink("espresso").cost = 1.5
    # Menu().find_drink("espresso").ingredients['water'] = 50
    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")


drink_menu = Menu()
menu_items = drink_menu.get_items() # latte/espresso/cappuccino/
espresso = drink_menu.menu[2].name # cappuccino
latte = drink_menu.find_drink("latte").name # latte

print(drink_menu.get_items()[2])


# Class with method**********************************************************************************************
# class User:
#     # Attributes
#     def __init__(self, user_id, username):
#         self.user_id = user_id
#         self.user_name = username
#
#         self.followers = 0
#         self.following = 0
#
#     # When a function is attached to a class/object it is called a method
#     # methods must always have a self parameter as the first parameter
#     # so that when the method is called, it knows the object that called it
#     # the self keyword is a way for us to refer to the object that is going
#     # to be created from the class inside the blueprint
#     # self is not used when you are using objects just when you are writing
#     # your code inside the class
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "Shannon")
#
# user_2 = User("003", "James")
# # print(user_1.user_id)
# # print(user_2.user_name)
# # print(user_2.followers)
#
# user_1.follow(user_2)
# print(user_1.followers)# 0
# print(user_1.following)# 1
# print(user_2.followers)# 1
# print(user_2.following)# 0


# Constructor: Initializing an Object*****************************************************************************
    # part of the blueprint that allows you to specify what should happen when the object is being
    # constructed/initialized
    # when an object is being initialized/ constructed you can set variables or counters with starting values
    # you create constructors using the __init__ function
            # has two underscores on each side of the name
            # special method that the Python interpreter knows about that
            # is normally used to initialize the attributes
    # class User:
    #     def __init__(self):
    #     #initialise attributes
    # self is that actual object that is being created/initialized
    # the __init__ function is going to be called everytime you create a new object from the class
    #******************************************************************************************
# # Class Declaration
# class User:
#     # whenever an object is constructed from this class it must be provided values for the parameters
#     # user_id and username
    # self is the actual object that is being created
#     def __init__(self, user_id, username): # parameters
#        # self.something: creates an attribute named something
#        # to be able to provide a value to the attributes when creating the object
#        # you must add parameters
#         self.user_id = user_id
#         self.user_name = username # user_name is an attribute
#         # you can name the attribute and the parameter whatever you want
#         # they do not have to be the same
#         # it is convention to name them the same, but you do not have to
#         # you call the attributes using the attribute name not the parameter name
#         self.followers = 0 # attribute with a default value
#         # because followers has a default value that is not a parameter we do not need to provide
#         # a value when creating the object
#         # all objects being created from this class will have an
#         # attribute followers with a default value of 0
#
#
# user_1 = User("001", "Shannon")
#
# user_2 = User("003", "James")
# print(user_1.user_id)
# print(user_2.user_name)
# print(user_2.followers)





# Within a Class Definition (Instance Attributes)***********************************************
# class MyClass:
#     def __init__(self, name, age):
#         self.name = name  # Creating 'name' attribute
#         self.age = age    # Creating 'age' attribute
#
# # Creating an object and assigning attributes
# my_object = MyClass("Alice", 30)
# print(my_object.name)
# print(my_object.age)

# Dynamically After Object Creation**************************************************************
# class User:
#     pass
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Shannon"
#
# user_2 = User()
# user_2.id = "003"
# user_2.username = "James"
# print(user_1.username)
# print(user_2.username)

# Class Attributes********************************************************************************
# class MyClass:
#     class_attribute = "Shared Value"
#
# obj1 = MyClass()
# obj2 = MyClass()
#
# print(obj1.class_attribute)
# print(obj2.class_attribute)


# Using setattr()**********************************************************************************
# class MyClass:
#     pass
#
# obj = MyClass()
# attribute_name = "dynamic_attribute"
# attribute_value = 123
# setattr(obj, attribute_name, attribute_value)
# print(obj.dynamic_attribute)