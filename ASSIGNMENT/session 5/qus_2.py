'''Build a class named FoodOrder that represents a Zomato-style order with properties: restaurant_name, items (a list), and total_price. Add a method show_order() that prints the order details in a readable format.'''

class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def show_order(self):
        print("----- Order Details -----")
        print("Restaurant:", self.restaurant_name)
        print("Items:")
        for item in self.items:
            print("-", item)
        print("Total Price: ₹", self.total_price)
        print("-------------------------")

# Creating an object
order1 = FoodOrder(
    "Pizza Hut",
    ["Margherita Pizza", "Garlic Bread", "Coke"],
    799
)

# Displaying order details
order1.show_order()