'''Simulate a Flipkart order summary calculator that takes price and quantity as input and calculates the total. Use try-except to handle ValueError if the user enters a non-numeric value, and display an error message.'''
 
# Flipkart Order Summary Calculator

try:
    # Take input from user
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Calculate total
    total = price * quantity

    # Display order summary
    print("\n----- Flipkart Order Summary -----")
    print("Price per item:", price)
    print("Quantity:", quantity)
    print("Total Amount:", total)

except ValueError:
    print("Error: Please enter only numeric values for price and quantity!")