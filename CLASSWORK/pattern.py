# # lines =5
# # for j in range(lines):
# #  for i range(lines):
# # print("*",end " ")
# # print()

# # lines = 10
# # for j in range(lines):
# #     print("*"*lines)
# lines = 5
# # for j in range(lines):
# #     for i in range(5):
# #         print("*"(j-1),end=" ")
# #     print()
# # lines = 5
# # for j in range(lines):
# #     for k in range(lines-(j-1)):
# #         print(" ",end=" ")

# #     for i in range(j+1):
# #         print("*",end=" ")
# #     print()
# #   *
# #  * *
# # * * * 
# # * * *
# #  * * 
# #   *
# lines = 5
# for j in range(lines):
#     for k in range(lines-j-1):
#         print(" ",end="")
#     for i in range(j+1):
#         print("* ",end="")
#     print()

# for j in range(lines-1):
#     for k in range(j+1):
#         print(" ",end="")
#     for i in range(lines-j-1):
#         print("* ",end="")
#     print()
#     # 1
#     # 12
#     # 123
#     # 1234
#     # 12345

# # 1
# # 23
# # 456
# # 78910

# #5
# #45
# #345
# #2345
# #12345

# #0
# #01
# #101
# #1010
# #10010
# lines = 5
# for j in range(lines):
#     for k in range(lines-j-1):
#         print(" ",end="")
#     for i in range(j+1):
#         print(i+1,end="")
#     print()
# lines = 5
# for j in range(lines):
#     for i in range(j+1):
#         print((i+j)%2,end="")

#     print()
# # home work
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
# #     *
# lines = 5
# for l in range(lines):
#     for h in range(lines-3):
#       print(" ",end="")
#     for s in range(l+1):
#       print("* ",end="")
#     print()
lines = 11
stars=1
spaces=lines
mid = (lines//2)+1
for i in range(1,lines+1):
    for k in range(1,spaces):
        print(" ",end="")
    for j in range(1,stars+1):
      if j==1 or j==stars:
         print("*",end="")
      else:
         print(" ",end="")
    print()
    if i<mid:
       stars+=2
       spaces-=1
    else:
       stars-=2
       spaces+=1
         
    



                
