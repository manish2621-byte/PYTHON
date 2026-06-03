print("program started")


try:

    a = 10
    b = a/0
    print(b)
except Exception as e:
    print(e)
else:
    print("code run successfully")
finally:
    print("always exceutable block")

print("program ended")
    

#Zerodivvisonerror
a = 10/0

#valueerror
st = "10.56"
k = float(St)
print(k)

#indexerror

l=[10,20,30]
print(l[3])

#keyerror

k = {"name":"john","age":30}
print(k['name'])
print(k.get("name1"))

#filenotfounderror
open("abc.txt","r")

#typeerror
print(10+10)
print("a"+"a")
print("a"+10)

#attributeerror
class demo:
    pass
d = demo()
print(d.a)

#nameerror
print(a)




