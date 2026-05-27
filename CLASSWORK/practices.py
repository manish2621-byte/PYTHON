

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

#isdisjoint
s1={1,2,3,4,5,6}
s2={7,8,9,10,11,12}
x=s1.isdisjoint(s2)
print(x)
