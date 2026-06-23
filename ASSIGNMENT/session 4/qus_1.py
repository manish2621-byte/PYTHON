'''Create a custom exception class called InvalidCouponCodeError for a Zomato-style food ordering app, and raise this exception if a user tries to apply a coupon code that is not in the list of valid codes.'''

# Custom Exception Class
class InvalidCouponCodeError(Exception):
    pass


# List of valid coupon codes
valid_coupons = ["ZOMATO50", "FOOD20", "SAVE100"]


# Function to apply coupon
def apply_coupon(coupon_code):
    if coupon_code not in valid_coupons:
        raise InvalidCouponCodeError("Invalid coupon code!")
    
    print("Coupon applied successfully!")


# Main Program
try:
    coupon = input("Enter coupon code: ")
    apply_coupon(coupon)

except InvalidCouponCodeError as e:
    print(e)