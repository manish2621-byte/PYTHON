

#DICTIONARY
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }

#clear
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }
# student.clear()

#copy
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }
# student1=student.copy()
# print(student1)

# #fromkeys
# d={"key1 ", "key2", "key3"}
# e=0
# f=dict.fromkeys(d,e)
# print(f)

 #get
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }
# print(student.get("course"))

# items
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }
# print(student.items())

#keys
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }
# print(student.keys())

#values
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }
# print(student.values())


#pop
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }
# student.pop("course")
# print(student)


#popitem
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }
# student.popitem()
# print(student)

#setdefault
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x=car.setupdate("color", "white")

# print(x)

# #update
# student={
#     "name" : "manish",
#     "course" : "python",
#     "age" : 23    
# }
# student.update({"course" : "java"})
# print(student)

# perfect square using reduce
from functools import reduce

# l = [1, 5, 6, 7, 8, 9, 4, 6, 5, 3, 4]

# perfect_squares = reduce(
#     lambda x, y: x + [y] if int(y**0.5) ** 2 == y else x,
#     l,
#     []
# )

# print(perfect_squares)

#  import math
# # l =[1,5,6,7,8,9,4,6,5,3,4]

# # k= filter(lambda x: math.isqrt(x)**2 == x,l)
# # print(list(k))

# l=[1,5,6,7,8,9,4,6,5,3,4]
# k= map(lambda x: x if math.isqrt(x)**2 == x else None,l)
# print(list(k))
# l = ["python", "java", "php", "andrioid"]

# result = list(filter(lambda x: "o" in x, l))

# print(result)
