# Practical Example 5: Write a Python program to find greater and less than a number using
#if_else.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)

elif num1 < num2:
    print(num1, "is less than", num2)

else:
    print("Both numbers are equal")

#Practical Example 6: Write a Python program to check if a number is prime using if_else.

number =20
flag =0
for i in range(2,number):
 if number%i==0:
    flag =1
    break
 if(flag==0):
    print("prime number")
 else:
    print("not prime number")

''' Practical Example 7: Write a Python program to calculate grades based on percentage using
if-else ladder.'''

percentage = float(input("Enter your percentage: "))

if percentage >= 90:
    print("Grade: A")

elif percentage >= 80:
    print("Grade: B")

elif percentage >= 70:
    print("Grade: C")

elif percentage >= 60:
    print("Grade: D")

elif percentage >= 50:
    print("Grade: E")

else:
    print("Grade: Fail")

''' Practical Example 8: Write a Python program to check if a person is eligible to donate blood
using a nested if.'''

age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))
health = input("Are you healthy? (yes/no): ")

if age >= 18:
    if age <= 65:
        if weight >= 50:
            if health == "yes":
                print("You are eligible to donate blood")
            else:
                print("Not eligible: Health condition not good")
        else:
            print("Not eligible: Weight is less than 50 kg")
    else:
        print("Not eligible: Age is above 65")
else:
    print("Not eligible: Age is below 18")


