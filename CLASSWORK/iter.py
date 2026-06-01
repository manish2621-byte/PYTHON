l = [10,20,30,40,50,60,70,80,90,100]

k = iter(l)
print(next(k))
print(next(k))

print(next(k))


def square(a):
    for i in range(a):
        yield i**2

r = square(10)
print(next(r))
print(next(r))
print(next(r))
print(next(r))