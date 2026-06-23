'''Simulate a Flipkart-style checkout process where a function process_payment(amount) raises a PaymentFailedError (custom exception) if the amount is less than or equal to zero, and prints 'Payment Successful' otherwise.'''

class PaymentFailedError(Exception):
    pass

def process_payment(amount):
    if amount <=0:
        raise PaymentFailedError("payment failed: amount must be greater than zero")
    print("payment successful")

try:
    process_payment(500)
    process_payment(0)
except PaymentFailedError as e:
    print(e)