# A=int(input("enter the first number: "))
# B=int(input("enter the second number: "))
# print(" 1 + \n 2 - \n 3 * \n 4 / \n 5 // \n 6 % \n 7 **")
# operator=input("enter the operator: ")
# match(operator):
#     case"+":
#         print("the sum is: ",A+B)
#     case"-":
#         print("the subtraction is: ",A-B)
#     case"*":
#         print("the multiplication is: ",A*B)
#     case"/":
#         print("the division is: ",A/B)
#     case"//":
#         print("the floor division is: ",A//B)
#     case"%":
#         print("the modulus is: ",A%B)
#     case"**":
#         print("the exponentiation is: ",A**B)
#     case _:
#         print("invalid operator ")
# for i in range(1, 11):
#print(i)
# i=20
# while(i<25):
#     print(i)
#   #  i+=1
# c="yes"
# while(c=="yes"):
# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))

# choice = input("enter the operator: ")
# match(choice):
#     case '+':
#         print(f"addtion of {a} and {b} is {a+b}")
#     case '-':
#         print(f"subtraction of {a} and {b} is {a-b}")
#     case '*':
#         print(f"multiplication of {a} and {b} is {a*b}")
#     case '/':
#         print(f"division of {a} and {b} is {a/b}")
#     case _ :
#         print("invalid operator")
#         c=input("do you want to continue: ")

c="yes"
while(c=="yes"):
    marks= int(input("enter your marks: "))
    if marks >= 91 and marks <= 100:
        print ("grade A")
    elif marks >=71 and marks <=90:
        print("grade b")
    elif marks >=51 and marks <=70:
        print("grade c")
    elif marks >=31 and marks <=50:
        print("grade d")
    elif marks >=0 and marks <=30:
        print("grade F")
    else: 
        print("invalid marks")
    c=input("do you want to continue: ")
