# KeyError, TypeError, FileNotFoundError, IndexError

# Exception Handling: Bare Except************************************************************************

# # if try fails do except
# try:
#     file = open("a_file.txt")

# except:# do not use bare 'except'
#     print("There was an error")

# when you have a bare except clause, it will ignore all errors***********************************************
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#
#     # because there is no "akey" key, this line fails and creates an exception(KeyError)
#      # But we will never see the KeyError Message because the except block catches it
#     print(a_dictionary["akey"])
# except:# this line catches the exception(KeyError), and the code inside is executed
#   # But this except code is not for the KeyError
#     file = open("a_file.txt", "w")
#     file.write("Something")

# except clause that is not bare will catch that error only***********************************************
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     # because there is no "akey" key, this line fails and creates an exception(KeyError)
#     print(a_dictionary["akey"])
#     # In this case, we will see the KeyError message
# except FileNotFoundError:# this except block only catches the FileNotFoundError
#     file = open("a_file.txt", "w")
#     file.write("Something")

# except clause to catch KeyError**********************************************
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["akey"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError:
#     print(f"The key does not exist.")
# #OR******************************************
# # except KeyError as error_message:#if we catch our exception and we still want to get hold of that error message
# #     print(f"The key {error_message} does not exist.")
# Else and Finally**********************************************************************************************
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:  # if no exceptions are thrown
#     content = file.read()
#     print(content)
# finally:  # not often used
#     file.close()
#     print("File was closed")


# Generate custom exceptions***************************************************************
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # To raise an exception you need to tap into one of the Exception Classes
#     raise TypeError("This is an error that I made up.")


#BMI Example: a case where you may want to rasie an error

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
