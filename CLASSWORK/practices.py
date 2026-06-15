# l=[]
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         l.append(str(i))
# print(','.join(l))

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number: "))
print(fact(n))
