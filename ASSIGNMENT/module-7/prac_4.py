'''Write a Python program to convert a list into a tuple'''

# Creating a list
my_list = [10, 20, 30, 40, 50]

my_tuple = tuple(my_list)
print("Original List:", my_list)
print("Converted Tuple:", my_tuple)


'''Write a Python program to create a tuple with multiple data types'''

# Creating a tuple with multiple data types
my_tuple = (100, 3.14, "Hello", True, 500, "Python")

print("Tuple with multiple data types:")
print(my_tuple)


'''Write a Python program to concatenate two tuples into one'''
# Creating two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result_tuple = tuple1 + tuple2

print("First Tuple:", tuple1)
print("Second Tuple:", tuple2)
print("Concatenated Tuple:", result_tuple)


''' Write a Python program to access the value of the first  index in a tuple.
'''
# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

first_element = my_tuple[0]

print("Tuple:", my_tuple)
print("First index element:", first_element)