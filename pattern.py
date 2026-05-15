# lines =5
# for j in range(lines):
#  for i range(lines):
# print("*",end " ")
# print()

# lines = 10
# for j in range(lines):
#     print("*"*lines)
lines = 5
# for j in range(lines):
#     for i in range(5):
#         print("*"(j-1),end=" ")
#     print()
# lines = 5
# for j in range(lines):
#     for k in range(lines-(j-1)):
#         print(" ",end=" ")

#     for i in range(j+1):
#         print("*",end=" ")
#     print()
#   *
#  * *
# * * * 
# * * *
#  * * 
#   *
lines = 5
for j in range(lines):
    for k in range(lines-j-1):
        print(" ",end="")
    for i in range(j+1):
        print("* ",end="")
    print()

for j in range(lines-1):
    for k in range(j+1):
        print(" ",end="")
    for i in range(lines-j-1):
        print("* ",end="")
    print()
    # 1
    # 12
    # 123
    # 1234
    # 12345

# 1
# 23
# 456
# 78910

#5
#45
#345
#2345
#12345

#0
#01
#101
#1010
#10010
lines = 5
for j in range(lines):
    for k in range(lines-j-1):
        print(" ",end="")
    for i in range(j+1):
        print(i+1,end="")
    print()
lines = 5
for j in range(lines):
    for i in range(j+1):
        print((i+j)%2,end="")

    print()



   
    

    


                
