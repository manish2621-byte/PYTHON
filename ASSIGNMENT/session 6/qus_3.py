'''Demonstrate multilevel inheritance by creating a class VerifiedInfluencer that inherits from Influencer and adds a badge attribute; create a VerifiedInfluencer object and display all its properties.'''

# Grandparent Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


# Parent Class
class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


# Child Class (Multilevel Inheritance)
class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge


# Create a VerifiedInfluencer object
v1 = VerifiedInfluencer(
    "manish2621",
    "manish2621@gmail.com",
    50000,
    "Blue Tick"
)

# Display all properties
print("Username:", v1.username)
print("Email:", v1.email)
print("Followers:", v1.followers)
print("Badge:", v1.badge)