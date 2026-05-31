'''Write a Python program to update a value at a particular key in a
dictionary'''

# Creating a dictionary
student = {
    "name": "Amit",
    "age": 21,
    "course": "BCA",
    "city": "Ahmedabad"
}

print("Original Dictionary:")
print(student)

student["city"] = "Surat"

print("\nUpdated Dictionary:")
print(student)


'''Write a Python program to separate keys and values from a dictionary using
keys() and values() methods'''

# Creating a dictionary
student = {
    "name": "pawan",
    "age": 19,
    "course": "pcm",
    "city": "Ahmedabad",
    "marks": 92
}

keys = student.keys()
values = student.values()

print("Dictionary:", student)
print("Keys:", keys)
print("Values:", values)


'''Write a Python program to convert two lists into one
dictionary using a for loop.'''

# Creating two lists
keys = ["name", "age", "city", "course"]
values = ["pawan", 20, "Ahmedabad", "pcm"]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print("Resulting Dictionary:")
print(my_dict)


'''Write a Python program to count how many times each
character appears in a string'''
# Taking input from user
text = input("Enter a string: ")

count_dict = {}

for char in text:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print("Character frequency:")
print(count_dict)