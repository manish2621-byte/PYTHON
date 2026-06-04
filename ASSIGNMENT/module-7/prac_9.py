''' Write a Python program to demonstrate the use of functions from
the math module.'''
# Demonstrate functions from the math module

import math

num = 16
x = 7.8

print("Square Root:", math.sqrt(num))
print("Power:", math.pow(2, 3))
print("Ceiling:", math.ceil(x))
print("Floor:", math.floor(x))
print("Factorial:", math.factorial(5))


'''Write a Python program to generate random numbers between 1 and
100 using the random module.'''

# Generate a random number between 1 and 100

import random

num = random.randint(1, 100)

print("Random Number:", num)