''' Write a Python program to iterate over a list using a for loop.
'''
# Creating a list
my_list = ["Apple", "Banana", "Mango", "Grapes"]

# Iterating over the list using for loop
print("Fruits in the list:")
for item in my_list:
    print(item)

''' Write a Python program to sort a list using both sort() and sorted().'''
# Creating a list
my_list = [40, 10, 30, 50, 20]

print("Original list:", my_list)

# Using sort() 
my_list.sort()
print("After sort():", my_list)

# Creating another list for sorted() example
new_list = [70, 60, 90, 80, 100]

print("\nNew list:", new_list)

# Using sorted() - returns a new sorted list
sorted_list = sorted(new_list)

print("After sorted():", sorted_list)
print("Original list remains unchanged:", new_list)