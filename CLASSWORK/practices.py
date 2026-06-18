# # a = 10
# # b = 20

# # sum = a + b
# # print(sum)

# # diff = a - b
# # print(diff)

# class Student:
# #    #default constructors
# #    def __init__(self):
#     college_name = "ABC college"
#     #parameterized constructors
#     def __init__(self,fullname,marks):
#         self.name = fullname
#         self.marks = marks
#         print("adding neww student in database. ")

#     def welcome(self):
#         print("welcome student,", self.name)
#     def get_marks(self):
#         return self.marks


# s1 = Student("priya goyani",89.85)
# print(s1.name,s1.marks)#priya goyani
# # s2 = Student("pawan goyani",80)
# # print(s2.name,s2.marks)#pawan goyani

# s1.welcome()
# print(s1.get_marks)




# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi",self.name, " your avg score is:", sum//3)

# s1 = Student("priya goyani", [99,98,97])
# s1.get_avg()