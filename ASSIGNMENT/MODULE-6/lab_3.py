#Write a Python program to demonstrate the creation of variables and different data types.

# Practical Example 1: How does the Python code structure work?

light = input("light :")
if light == "red":
    print("stop")
elif light == "yellow":
    print("ready")
elif light == "green":
    print("go")
else:
    print("invalid light")

#Practical Example 2: How to create variables in Python?

name = "manish"
age = 23
height = 5.8

print(name)
print(age)
print(height)

#Practical Example 3: How to take user input using the input() function

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name)
print("Your age is", age)

#Practical Example 4: How to check the type of a variable dynamically using type().

a = 10
b = 5.5
c = "Python"
d = [1, 2, 3]

print(type(a))
print(type(b))
print(type(c))
print(type(d))