'''Write a Python program to create a list with elements of multiple data types (integers,
strings, floats, etc.).'''
# Creating a list with multiple data types
my_list = [10, 20.5, "Hello", "Python", 100, 3.14, True]

print("List with multiple data types:")
print(my_list)

print("\nData types of each element:")
for item in my_list:
    print(item, "->", type(item))



''' Write a Python program to access elements at different index positions.'''

# Creating a list
my_list = [10, 20, 30, 40, 50, 60]

 #positive indexing
print("Element at index 0:", my_list[0])
print("Element at index 2:", my_list[2])
print("Element at index 4:", my_list[4])

#negative indexing
print("Element at index -1 (last element):", my_list[-1])
print("Element at index -3:", my_list[-3])

# Accessing multiple elements (slicing)
print("Elements from index 1 to 4:", my_list[1:5])