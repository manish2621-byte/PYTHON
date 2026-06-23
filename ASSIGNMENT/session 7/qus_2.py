# Parent Class
class Payment:
    def pay(self, amount):
        print(f"Paying {amount}")

# Child Class
class UPI(Payment):
    def pay(self, amount):
        print(f"Paying {amount} via UPI")

# Create objects
p = Payment()
u = UPI()

# Call pay() method
p.pay(500)
u.pay(500)