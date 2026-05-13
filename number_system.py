# convert decimal number into the binary number
dec_num=int(input("enter your decimal number: "))

power = 1
ans = 0

while dec_num > 0:
    rem = dec_num % 2
    dec_num = dec_num // 2
    ans += (rem * power)
    power *= 10

print(ans)


bin_num=int(input("enter your binary number: "))

power = 1
ans = 0

while bin_num > 0:
    rem = bin_num % 10
    ans += (rem * power)
    bin_num //= 10
    power *= 2

print(ans)