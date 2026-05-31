''' Write a Python program to create a function that takes a string as input and prints it.'''
# Defining a function
def print_string(text):
    print("You entered:", text)

user_input = input("Enter a string: ")


print_string(user_input)


''' Write a Python program to create a calculator using functions.
'''
# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")

