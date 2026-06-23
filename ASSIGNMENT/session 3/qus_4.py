'''Given the following buggy code, fix it so that it catches both IndexError and KeyError and prints a custom message for each:<br><br>my_list = [1, 2, 3]
print(my_list[5])
my_dict = {'a': 1}
print(my_dict['b'])<br><br><em><strong>Hint:</strong> Use multiple except clauses to handle each exception separately.</em>'''


my_list = [1, 2, 3]
my_dict = {'a': 1}

# Handle IndexError
try:
    print(my_list[5])
except IndexError:
    print("Error: List index is out of range!")

# Handle KeyError
try:
    print(my_dict['b'])
except KeyError:
    print("Error: Key not found in dictionary!")