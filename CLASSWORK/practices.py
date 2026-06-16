# l=[]
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         l.append(str(i))
# print(','.join(l))

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter a number: "))
# print(fact(n))
 

# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(1, 2)

# calc_sum(12, 5)

# calc_sum(45, 78)

# def aver_3(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# aver_3(98, 97, 95)

cities = ["delhi", "surat","mumbai","bangluru","chennai"]
heroes = ["thor", "ironman","captain america","shaktiman"]

# def items(list):
#     for item in list:
#         print(item,end=" ")

# items(cities)

# items(heroes)

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x=int(input())
# print(fact(x))

# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i

# print(d)

# values =input()
# l=values.split(",")
# t=tuple(l)
# print(l)
# print(t)


# class inputoutstring(object):
#     def __init__(self):
#         self.s =""
#     def getstring(self):
#         self.s = input()
#     def printstring(self):
#         print(self.s.upper())

    
# strObj = inputoutstring()
# strObj.getstring()
# strObj.printstring()

# import math
# c=50
# h=30
# value = []
# items=[x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(value))


# class Test:
#     id = 10
#     _name="manish"
#     __email="manish@gmail.com"


# t = Test()
# print(dir(t))
# print(t.id)
# print(t._Test__email)

class Student:
    __id = 10

    def get_id(self):
        return self.__id

    def set_id(self,a):
        self.__id = a



    s = Student()   
    s.set_id(100)
    print(s.get_id())