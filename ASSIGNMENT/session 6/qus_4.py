'''Implement multiple inheritance by creating a class BrandPartner that inherits from both Influencer and a new class Brand (with attribute brand_name); create a BrandPartner object and print the username, followers, and brand_name.'''

# First Parent Class
class Influencer:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers

# Second Parent Class
class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name

# Child Class (Multiple Inheritance)
class BrandPartner(Influencer, Brand):
    def __init__(self, username, followers, brand_name):
        Influencer.__init__(self, username, followers)
        Brand.__init__(self, brand_name)

# Create a BrandPartner object
bp = BrandPartner("vk", 9603, "one8")

# Print details
print("Username:", bp.username)
print("Followers:", bp.followers)
print("Brand Name:", bp.brand_name)