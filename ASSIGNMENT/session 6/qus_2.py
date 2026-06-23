'''Build a single inheritance example where a class Influencer inherits from User and adds a followers attribute; create an Influencer object and print all its details.'''
# Parent Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# Child Class
class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

# Create an Influencer object
inf1 = Influencer("techguru", "techguru@gmail.com", 50000)

# Print details
print("Username:", inf1.username)
print("Email:", inf1.email)
print("Followers:", inf1.followers)
