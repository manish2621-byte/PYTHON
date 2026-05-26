# # list append
# fruits=["apple","mango","watermelon"]
# fruits.append("banana")
# print(fruits)

# #clear
# fruits=["apple","mango","watermelon"]
# fruits.clear()
# print(fruits)

# #copy
# fruits=["apple","mango","watermelon"]
# x=fruits.copy()
# print(x)

# #extend
# car=["porche","BMW","audi","volvo","merchedes"]
# fruits=["apple","mango","watermelon"]
# car.extend(fruits)
# print(car)


# #index
# fruits=["apple","mango","watermelon"]
# a=fruits.index("mango")
# print(a)
    
# #insert
# fruits=["apple","mango","watermelon"]
# fruits.insert(0,"banaana")
# print(fruits)

# #reverse
# fruits=["apple","mango","watermelon"]
# fruits.reverse()
# print(fruits)

# cars = ['Ford', 'BMW', 'Volvo']

# cars.sort()

# print(cars)

#loop list

# fruits=["apple","mango","watermelon"]
# for a in fruits:
#     print(a)

# # len and range

# fruits=["apple","mango","watermelon"]
# # for a in range(len(fruits)):
# #     print(a)
# i=0
# while i < len(fruits):
#     print(fruits[i])
#     i=+1

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# #list comprehension
# thislist = ["apple", "banana", "cherry"]
# # [print(x) for  x in thislist]
# y = list(thislist)
# y[0] = "mango"
# thislist = tuple(y)
# print(thislist)


# #set difference

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.difference(y)

# print(z)

# # difference update
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.difference_update(y)
# print(x)

# #discard
# fruits = {"apple", "banana", "cherry"}

# fruits.remove("banana")

# print(fruits)

# # issubset
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}

# z = x.issubset(y)

# print(z)

#union

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.union(y)

# print(z)

list1=[5,4,3,2,1]
# list1.append(list2)
# print(list1)list2=[7,8,9,5,9,10]

print(list1.sort())
print(list1)