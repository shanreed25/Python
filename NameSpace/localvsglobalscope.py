# global scope variable
enemies = 1
# variable set to 1

def increase_enemies():
    # local scope variable
    enemies = 2
    # same variable set to 2
    print(f"enemies inside function: {enemies}")


increase_enemies() #this enemies variable refers to the local scope enemies
#this enemies variable refers to the global scope enemies
print(f"enemies outside function: {enemies}")

#****************************************************************************************************
# Local Scope Variable
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()

# Can't access this potion_strength outside its local scope
print(potion_strength)
#****************************************************************************************************
# Global Scope Variable
# available anywhere in the file because it was defined at the top level of the file
# top level does not mean at the top of the file it just means it is defined outside a function or method
player_health = 10

def drink_new_potion():
        potion_strength = 2
        print(player_health)


drink_new_potion()

print(player_health)

#****************************************************************************************************
# Local scope function
def game():
    def drink_another_potion():
        potion_strength = 2
        print(player_health)

    drink_another_potion()


# Can't access this drink_another_potion function outside
# its local scope which is the game function
drink_another_potion()

#***********************************************************************************************************
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

# when we crate variables inside any block of code such as if statement or for loop
# that variable is in the same scope as the statement it is inside of
if game_level < 5:
    # this if statement is in global scope and so is new_enemy
    new_enemy = enemies[0]

print(new_enemy)

if game_level == 15:
    # this if statement is in global scope and so is new_enemy
    my_new_enemy = enemies[0]

# NameError: name 'new_enemy' is not defined,
# because game_level is not 15 the my_new_enemy is never created
print(my_new_enemy)

# to prevent the error from above (NameError: name 'new_enemy' is not defined)
# you can create a variable outside the if statement and set it to empty
my_worst_enemy = ""
if game_level == 15:
    my_worst_enemy = enemies[0]


print(my_worst_enemy)
#***********************************************************************************************
def create_enemy():
    another_new_enemy = ""
    if game_level < 5:
        # this variable is in the same scope as the create_enemy function which is global scope
        another_new_enemy = enemies[0]
    # this will not work
    print(another_new_enemy)
# This will cause a NameError: name 'another_new_enemy' is not defined
print(another_new_enemy)
