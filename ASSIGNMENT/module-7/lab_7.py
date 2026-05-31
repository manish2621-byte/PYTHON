''' Write a Python program to update a value in a dictionary.'''
# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA",
    "marks": 75,
    "city": "Ahmedabad"
}

print("Original Dictionary:")
print(student)

student["marks"] = 85
student["city"] = "Surat"

print("\nUpdated Dictionary:")
print(student)


''' Write a Python program to merge two lists into one dictionary using a loop'''

# Creating two lists
keys = ["name", "age", "city", "course"]
values = ["Rahul", 20, "Ahmedabad", "BCA"]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print("Dictionary after merging lists:")
print(my_dict)