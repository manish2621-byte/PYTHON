"""Write a Python program that demonstrates the correct use of indentation, comments, and
variablesfollowing PEP 8 guidelines."""
#calculate the persentage  of student
student_name="manish sharma"
science_marks=80
math_marks=75
social_marks=77
english_marks=72
hindi_marks=85
total= science_marks+math_marks+social_marks+english_marks+hindi_marks
persentage= total/500*100
print("your average marks is",persentage)
 
 # CALCULATOR 
a=55
b=20
print("operator is +,-,/,//,%,**")
operator=input("enter your operator : ")
if(operator == '+'):
    print("addition is ",a+b)
elif(operator == '-'):
    print("substraction is ",a-b)
elif(operator == '/'):
    print("divison is ",a/b)
elif(operator == '//'):
    print("floor divison is ",a//b)
elif(operator == '%'):
    print("modulos is ",a%b)
elif(operator == '**'):
    print("exponentitation ",a**b)