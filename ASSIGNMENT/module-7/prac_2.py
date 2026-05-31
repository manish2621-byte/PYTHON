'''Write a Python program to update a list using insert() and
append().'''
# Creating a list
my_list = [10, 20, 30]

print("Original list:", my_list)

# Updating list using append() 
my_list.append(40)
my_list.append(50)

print("After using append():", my_list)

# Updating list using insert() 
my_list.insert(1, 15)   
my_list.insert(3, 25)   

print("After using insert():", my_list)


'''Write a Python program to remove elements from a list using pop() and
remove().'''
# Creating a list
my_list = [10, 20, 30, 40, 50, 30]

print("Original list:", my_list)

my_list.remove(30)
print("After remove(30):", my_list)

removed_item = my_list.pop(2)   

print("After pop(2):", my_list)
print("Removed element using pop():", removed_item)