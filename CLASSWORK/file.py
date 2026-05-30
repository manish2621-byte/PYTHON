
f = open("test.txt", "w")

f.write("hello python\n")
f.write("python\njava\nc++\n")

f.close()


f = open("test.txt", "r")

data = f.read()

print(data)

f.close()


f = open("test.txt", "r")

while True:
    data = f.readline()

    if not data:
        break

    if data.startswith("p"):
        print(data)

f.close()


# SEEK AND TELL
with open("test.txt", "r") as f:

    f.seek(5)          

    print(f.tell())    

    data = f.read()

    print(f.tell())   

    print(data)


# APPEND 
with open("test.txt", "a") as f:

    f.write("hello manish\n")


with open("test.txt", "r") as f:

    data = f.read()

    print(data)


import json
k = {"name": "abc", "age": 20, "city": "delhi"}

with open("data.json", "w") as f:
    json.dump(k,f)


with open("data.json", "r") as f:
    k = json.load(f)
    print(k)



