''' Practical Example 1: Write a Python program to print each fruit in a list using a simple for
loop. List1 = ['apple', 'banana', 'mango']'''
# List of fruits
List1 = ['apple', 'banana', 'mango']

# Using for loop to print each fruit
for fruit in List1:
    print(fruit)


''' Practical Example 2: Write a Python program to find the length of each string in List1.'''
# List of strings
List1 = ['apple', 'banana', 'mango']

# Finding length of each string using for loop
for fruit in List1:
    print(fruit, ":", len(fruit))


''' Practical Example 3: Write a Python program to find a specific string in the list using a simple
for loop and if condition.
'''
# List of fruits
List1 = ['apple', 'banana', 'mango']

search_item = input("Enter fruit to search: ")

found = False

for fruit in List1:
    if fruit == search_item:
        found = True
        break

# Check result
if found:
    print(search_item, "is found in the list")
else:
    print(search_item, "is NOT found in the list")

    '''Practical Example 4: print this pattern using nested loop'''
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    lines=5
    for j in range(lines):
     for i in range(j + 1):
         print("*",end=" ")
     print()