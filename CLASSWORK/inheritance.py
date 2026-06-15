# # Parent / Super / Base Class
# class A:
#     A = 10

#     def display(self):
#         print("in A")


# class B(A):
#     B = 20

#     def display(self):
#         print("show calling")
#         # print(self.A)      # Access parent class variable
#         print(A.A)         # Access parent class variable directly


# b = B()
# b.display()


# class Pen:

#     def __init__(self, price, color, company):
#         self.price = price
#         self.color = color
#         self.company = company

#     def display(self):
#         print(self.color, self.company, self.price)


# class Notebook(Pen):

#     def __init__(self, price, color, company, pages):
#         super().__init__(price, color, company)
#         self.pages = pages

#     def display(self):
#         print(self.color, self.price, self.company, self.pages)


# p = Pen(100, "RED", "Cello")
# p.display()

# n = Notebook(200, "Blue", "Classmate", 200)
# n.display()








    