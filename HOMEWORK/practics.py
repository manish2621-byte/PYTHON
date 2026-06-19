# # from abc import ABC, abstractmethod

# # class Account(ABC):

# #     def __init__(self, loan):
# #         self.balance = loan

# #     @abstractmethod
# #     def deposit_loan(self, amount):
# #         pass

# #     @abstractmethod
# #     def withdraw_loan(self, amount):
# #         pass


# # class Saving(Account):

# #     def deposit_loan(self, amount):
# #         self.balance -= amount

# #         if self.balance <= 0:
# #             print("Loan fully paid")
# #             self.balance = 0

# #     def withdraw_loan(self, amount):
# #         self.balance += amount


# # s = Saving(10000)

# # print("Loan:", s.balance)

# # s.deposit_loan(5000)
# # print("Remaining Loan:", s.balance)

# # s.deposit_loan(5000)
# # print("Remaining Loan:", s.balance)
 

# #abstraction

# # class car:
# #     def __init_(self):
# #         self.acc = False
# #         self.brk = False
# #         self.clutch = False
# #     def start(self):
# #         self.clutch = True
# #         self.acc = True
# #         print("car started..")


# # car1 = car()
# # car1.start()

# #eapcapsulation
# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no =acc
#     #debit
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance = ",self.get_balance())

#     #credit
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance = ",self.get_balance())

#     #balance
#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000,12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(9500.52)


# class Student: 
#     def __init__(self,name):
#         self.name = name


# s1 = Student("vivek")
# print(s1.name)
# del s1.name
# print(s1.name)
 
# class Account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

    

# acc1 = Account("12345","abcde")
# print(acc1.acc_no)
# print(acc1.__acc_pass)

# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# p1.welcome()

#inheritance
# class Car:

#  @staticmethod
#  def start():
#   print("car started..")

#   @staticmethod
#   def stop():
#    print("car stopped.")

# class ToyotaCar(Car):
#   def __init__(self, name):
#       self.name = name


# car1 = ToyotaCar("FORTUNER")
# car2 = ToyotaCar("prius")

# print(car1.start())


class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

