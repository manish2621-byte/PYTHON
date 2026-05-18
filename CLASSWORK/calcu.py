A=int(input("enter the first number: "))
B=int(input("enter the second number: "))
print(" 1 + \n 2 - \n 3 * \n 4 / \n 5 // \n 6 % \n 7 **")
operator=input("enter the operator: ")
match(operator):
    case"+":
        print("the sum is: ",A+B)
    case"-":
        print("the subtraction is: ",A-B)
    case"*":
        print("the multiplication is: ",A*B)
    case"/":
        print("the division is: ",A/B)
    case"//":
        print("the floor division is: ",A//B)
    case"%":
        print("the modulus is: ",A%B)
    case"**":
        print("the exponentiation is: ",A**B)
    case _:
        print("invalid operator ")