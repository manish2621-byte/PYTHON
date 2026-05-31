'''Write a Python program to iterate through a list and print each
element'''
# Creating a list
my_list = [10, 20, 30, 40, 50]

print("Elements in the list:")
for element in my_list:
    print(element)



''' Write a Python program to insert elements into an empty list using a for loop and
append().'''
# Creating an empty list
my_list = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = input("Enter element: ")
    my_list.append(value)

# Printing final list
print("Final list:", my_list)