
#*****************************************LIST COMPREHENSIONS**************************************************************
#------------Creating List from Dictionary
bids = {
    "Shannon": 215.0,
    "Lisa": 124.0,
    "James": 119.0,
    "Molly": 220.0,
    "Mike": 212.0,
}

#*********************List of Dictionaries*********************
bids_dict_list = [{key:value} for (key, value) in bids.items()]
print(f"List of Dictionaries: {bids_dict_list}")

#*********************List of Tuples***************************
bids_list = [item for item in bids.items()]
# list of tuples each with a key and value
print(f"List of Tuples: {bids_list}")
#*********************List of Dictionary Values****************
bids_list = [value for (key, value) in bids.items()]
# list of all the values
print(f"List of Dictionary Values: {bids_list}")

#*********************List of Dictionary Keys*******************
bids_list = [key for (key, value) in bids.items()]
# list of all the keys
print(f"List of Dictionary Keys: {bids_list}")

# # using a dictionary key as new item: Passing in each item from a list as a key to the dictionary
# - **Keword Method:** `[new_item for item in list]`
# ```
# my_dict = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot'}
# my_list = ['B', 'C', 'D']

# dict_values_list = [my_dict[letter] for letter in my_list]
# print(dict_values_list)# ['Bravo', 'Charlie', 'Delta']
