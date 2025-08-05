#**************************Create Empty/Wipe Entire Dictionary*********************************************
# You create an empty dictionary and wipe an exsiting dictionary using the same syntax
emp_phone_numbers = {}

#**************************Create Dictionary with content**************************************
emp_phone_numbers = {"Lisa": 1234567890, "James": 9876540321, "Kim": 5673456288}

#**************Editing Items and Adding new items to an existing dictionary********************
emp_phone_numbers["Mary"] = 5432345678
#Adding New item: if there is no key "Mary" then it's going to create a new entry with the new key and value
#Editing item:  if there is a key "Mary" already in the dictionary then it will change the value to the new value


#********************************Removing Items by index:pop()**********************
emp_phone_numbers.pop("James")#returns 9876540321(value of James)
# if the key is not found it will cause a KeyError, use default value to avoid KeyError
emp_phone_numbers.pop("Kate", "There is no Kate")# will return There is no Kate

#***********************************max()*******************************************
bids = {
    "Shannon": 215.0,
    "lisa": 124.0,
    "James": 119.0,
    "Molly": 220.0,
    "Mike": 212.0,
}
# Returns the Key with the highest price as the value
max_value = max(bids, key=bids.get)
print(max_value)#returns Molly


#**************************************Looping Through Dictionaries**********************************************

student_dict = {
    "students": ["James", "Lisa", "Rita", "Keon", "Rider"],
    "scores": [89, 76, 82, 100, 73]
}


#*********************Iterate through a dictionary ***************************
for key in student_dict:
    # prints a list of values for each key
    print(student_dict[key])


for (key, value) in student_dict.items():
        #prints each key with a list of values
        print(key, value)



for (key, value) in student_dict.items(): #adds unnecessary parentheses and is less common in modern Python code
      pass
#the code above and below have the exact same functionality
for key, value in student_dict.items(): #the preferred and idiomatic way: in current Python versions (Python 3 and later) due to its conciseness and clarity
      pass



# Accessing Values