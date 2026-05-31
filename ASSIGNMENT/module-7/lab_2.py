''' Write a Python program to add elements to a list using insert() and append().'''

# Creating an empty list
my_list = []

# Adding elements using append() 
my_list.append(10)
my_list.append(20)
my_list.append(30)

print("After using append():", my_list)

# Adding elements using insert()
my_list.insert(1, 15)   
my_list.insert(0, 5)    

print("After using insert():", my_list)

''' Write a Python program to remove elements from a list using pop() and remove().'''

# Creating a list
my_list = [10, 20, 30, 40, 50, 30]

print("Original list:", my_list)

# Using remove() - removes first matching value
my_list.remove(30)
print("After remove(30):", my_list)

# Using pop() - removes element by index
removed_element = my_list.pop(2)  # removes element at index 2

print("After pop(2):", my_list)
print("Removed element using pop():", removed_element)

