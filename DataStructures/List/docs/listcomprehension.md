



```
#Using List Comprehension (Recommended for general cases):
# creates a new list containing only the elements from a that are not present in b
# missed_states = [item for item in states_column_list if item not in user_answer_list]
# OR
# use a for loop and if statement
missed_states = []
for state in states_column_list:
    if state not in user_answer_list:
        missed_states.append(state)
```