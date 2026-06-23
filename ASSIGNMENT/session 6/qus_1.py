'''Create a Python class called User with attributes username and email, then create an object and print its details.'''
class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

# Create an object
user1 = User("manish123", 23)

# Print details
print("Username:", user1.username)
print("Email:", user1.age)

