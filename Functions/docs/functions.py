def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

def my_function(a):
    if a < 40:
        return# a = 25 retuns "None" because this line will exit the function and the rest of the code will not run
        print("Terrible")# this will never run
    if a < 80:
        return "Pass" # a = 55 will return "Pass"
    else:
        return "Great"
print(my_function(515))


def add(n1, n2):
    return n1 + n2

my_add_function = add
print(my_add_function(3, 5)) # Will return 8