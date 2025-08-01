class Dog:
    def __init__(self):
        self.temperament = "loyal"
 
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "sweet"

my_dog = Dog()
print(f"My dog is {my_dog.temperament}")
 
my_other_dog = Labrador()
print(f"My other dog is {my_other_dog.temperament}")