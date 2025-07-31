# Class with a Arbitrary Number of Arguments
- classes whose methods, particularly the __init__ constructor, are designed to accept a variable number of arguments using the *args and/or **kwargs syntax, providing flexibility in how instances are created and how their methods are invoked





# class Car:
#     def __init__(self, **kwargs):
#         # if we use kwargs this way and the key does not exist
#         # you will get a KeyError
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]
#
#
# new_car = Car(make="Chevrolet", model="Tahoe")
# my_car = Car(make="Chevrolet" )
# print(my_car.model)# KeyError: 'model'


# class Car:
#     def __init__(self, **kwargs):
#         # Dictionaries
#        # by using .get() instead of kwargs[] we can avoid the KeyError
#         self.make = kwargs.get("model")
#         self.model = kwargs.get("model")
# 
# 
# my_car = Car(make="Chevrolet")
# print(my_car.model)# None
#     # Dictionaries
#     # we can also use a function called get()
#     # pass in the name of the key if we want to get hold of the value
#     # benefit is that if the ksy does not exist in the dictionary, it will return none, instead of giving a KeyError